import jieba
import os

def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='gbk').readlines()]
    return stopwords


def sentiment_dict(filepath):
    """读取情感词典"""
    res = {}
    with open(filepath, encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            if line.strip():
                k, v = line.split()
                res[k] = float(v)
    return res


# 对句子去除停用词
def movestopwords(sentence):
    stopwords = stopwordslist(os.path.join(os.path.abspath("."),'stopword.txt'))  # 这里加载停用词的路径
    outstr = ''
    for word in sentence:
        if word not in stopwords:
            if word != '\t' and '\n':
                outstr += word
    content_seg = jieba.cut(outstr)
    return content_seg


def get_top_positive_negative_frequency(data, top=10):
    """
    获取top n个消极词汇与积极词汇以及词频
    :param data: 评论数据
    :param top:
    :return:
    """
    senti_dict = sentiment_dict(os.path.join(os.path.abspath("."),'BosonNLP_sentiment_score.txt'))
    print(os.path.join(os.path.abspath("."),'BosonNLP_sentiment_score.txt'))
    content_seg = movestopwords(data["comments"])
    scores = {}
    frequency = {}
    for word in content_seg:
        scores[word] = senti_dict.get(word, 0)
        if frequency.get(word):
            frequency[word] += 1
        else:
            frequency[word] = 1
    scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    frequency = dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))
    positive = dict(scores[0:top])
    negative = dict(scores[-top:])
    return {
        "positive": positive,
        "negative": negative,
        "frequency": frequency
    }


if __name__ == '__main__':
    # 读取nlp情感词分数
    from utils import get_data

    data = get_data("lzh","1512002")
    print(get_top_positive_negative_frequency(data,15))
