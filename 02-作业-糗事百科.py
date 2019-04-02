from urllib import request
import time
import re

# 作业2: 爬取糗事百科文本页的所有段子,结果如 : xx说: xxxx
# https://www.qiushibaike.com/text/page/1/   # 1表示页码

# 正则表达式提示： 
#	# 获取一个评论
#   regCom = re.compile('<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">', re.S)
#	# 获取名称
#   nameCom = re.compile('<h2>(.*?)</h2>', re.S)
#	# 获取内容
#	contentCom = re.compile('<span>(.*?)</span>', re.S)


def getData(url):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

    req = request.Request(url=url,headers=headers)
    response = request.urlopen(req)
    content = response.read().decode()

    regCom = re.compile('<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">', re.S)
    qiushi_list = regCom.findall(content)

    for qiushi in qiushi_list:
        # 获取名称
        nameCom = re.compile('<h2>(.*?)</h2>', re.S)
        name = nameCom.findall(qiushi)[0].strip()

        # 获取内容
        contentCom = re.compile('<span>(.*?)</span>', re.S)
        content = contentCom.findall(qiushi)[0].strip()

        print("%s说：%s" % (name, content))

if __name__ == "__main__":
    for i in range(1, 4):
        url = "https://www.qiushibaike.com/text/page/" + str(i) + "/"
        getData(url)
        time.sleep(0.5)






