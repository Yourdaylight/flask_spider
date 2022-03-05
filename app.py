# encoding:utf-8
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from text_analysis.code import get_top_positive_negative_frequency
from utils import get_data

app = Flask(__name__)
# 连接数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/flask_spider'
# 实例化orm框架的操作对象，后续数据库操作，都要基于操作对象来完成
db = SQLAlchemy(app)


# 声明模型类
class User(db.Model):
    __tablename__ = "tb_user"  # 设置表名
    id = db.Column(db.INTEGER, primary_key=True)
    username = db.Column(db.String(16), nullable=False)
    password = db.Column(db.String(16), nullable=False)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/login", methods=["post"])
def login():
    """登录"""
    code, msg = 200, "success"
    username = request.json.get("username")
    password = request.json.get("password")
    if not username or not password:
        code, msg = 500, "用户名或者密码不能为空"
    if not User.query.filter_by(username=username, password=password).first():
        code, msg = 500, "密码错误"
    return jsonify({"msg": msg, "code": code})


@app.route("/regist", methods=["post"])
def regist():
    """注册"""
    code, msg = 200, "success"
    username = request.json.get("username")
    password = request.json.get("password")
    if username and password:
        if User.query.filter_by(username=username).first():
            msg = "用户%s已存在" % username
        else:
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
    return jsonify({"msg": msg, "code": code})


@app.route("/display", methods=["post"])
def display():
    """
    获取绘图数据
    :return:
    """
    code, msg = 200, "success"
    url = request.json.get("url")
    username = request.json.get("username")
    top = request.json.get("top", 10)
    product_id = url.split('id=')[-1] if url.split('id=') else url
    data = get_data(username, product_id)
    data.update(get_top_positive_negative_frequency(data, top))
    data.pop("comments")
    return jsonify({"msg": msg, "code": code, "data": data})


if __name__ == '__main__':
    db.create_all()
    app.run(host="0.0.0.0")
