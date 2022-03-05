# -*- coding: utf-8 -*-
import time
import traceback

import pymysql
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}


class dbutil:

    def __init__(self):
        self.db = pymysql.connect(host='127.0.0.1',
                                  user='root',
                                  password='123456',
                                  database='flask_spider')

    def insert(self, sql):
        # 打开数据库连接

        # 使用cursor()方法获取操作游标
        cursor = self.db.cursor()
        # SQL 插入语句
        try:
            # 执行sql语句
            cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            traceback.print_exc()
            self.db.rollback()
        self.db.close()

    def search(self, sql):
        try:
            # 执行SQL语句
            cursor = self.db.cursor()
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            return results
        except:
            traceback.print_exc()


def parse_comments(username, product_id, page_limit=20):
    """
    爬取评论数据
    username: 用户名
    product_id: 产品名称
    page_limit: 爬取页数，这里默认最大设置为20
    """
    comments_url = "https://you.163.com/xhr/comment/listByItemByTag.json?__timestamp={}&itemId={}&size=20&page={}&orderBy=0".format(
        time.time() * 1000, product_id, 1)
    res = requests.get(comments_url, headers=headers).json()
    if res:
        pages = res.get("data", {}).get("pagination", {}).get("totalPage", 1)
        # 我们这里最多只爬取page_limit页，一次爬多容易触发反爬虫机制
        pages = pages if pages <= page_limit else page_limit
        for page in range(1, pages + 1):
            comments_url = "https://you.163.com/xhr/comment/listByItemByTag.json?__timestamp={}&itemId={}&size=20&page={}&orderBy=0".format(
                time.time() * 1000, product_id, page)
            res = requests.get(comments_url, headers=headers).json()
            for item in res.get("data", {}).get("commentList", []):
                try:
                    comment = item.get("content", "")
                    update_time = item.get("createTime", -1)
                    sql = "insert into tb_comments(username,url,product_id,comment,update_time) values ('{}','{}','{}','{}',{});".format(username, comments_url,product_id,comment, update_time)
                    dbutil().insert(sql)
                except Exception as e:
                    traceback.print_exc(e)


def parse_tags(username, product_id):
    """
    爬取评论的标签，以及标签数量
    username: 用户名
    product_id: 产品名称
    """
    tags_url = "https://you.163.com/xhr/comment/tags.json?__timestamp={}&itemId={}".format(time.time() * 1000, product_id)
    res = requests.get(tags_url, headers=headers).json()
    for item in res.get("data", {}):
        try:
            tag = item.get("name", "")
            count = item.get("strCount", 0)
            sql = "insert into tb_tags(username,url,product_id,tag,count,update_time) values ('{}','{}','{}','{}',{},{});".format(username, tags_url, product_id,tag, count,
                                                                                                                  int(time.time()))
            dbutil().insert(sql)
        except Exception as e:
            print(sql)
            traceback.print_exc(e)


def get_data(username, product_id):
    """
    检查这个product_id是否爬取过，爬取过的评论会在数据库中保存，直接取出来分析即可,如果没有则进行爬取
    :param username:
    :param product_id:
    :return:
    """
    sql = "select * from {} where product_id='{}' and username='{}'"
    res = {
        "tags": {},
        "comments": None
    }
    # 如果有返回值
    rtn = dbutil().search(sql.format("tb_comments", product_id, username))

    if rtn:
        pass
    # 如果没有返回值，说明没有爬取，这里开始爬取评论数据
    else:
        parse_comments(username, product_id)
        parse_tags(username, product_id)
        rtn = dbutil().search(sql.format("tb_comments", product_id, username))
    # 统一处理数据返回
    # 获取商品的所有评论，查tb_comments表
    res["comments"] = "".join([i[2] for i in rtn])
    # 获取商品的各种评论标签以及对应数量，查tb_tags表
    tags = dbutil().search(sql.format("tb_tags", product_id, username))
    if tags:
        for tag in tags:
            _tag, count = tag[2], tag[3]
            res["tags"][_tag] = count
    return res


if __name__ == '__main__':
    # parse_tags("lzh", "1085007")
    # check_exists("lzh", "1085007")
    print(get_data("lzh", "1085007"))
