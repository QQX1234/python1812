import json
import re
import ssl

import requests
from bs4 import BeautifulSoup

#####第一层
def first_cwawl(url,params,headers):


    response = requests.get(url, params=params, headers=headers)

    req = response.text

    soup = BeautifulSoup(req, 'lxml')
    td_list = soup.find_all(name='td', attrs={'class': 'l square'})
    # print(td_list)
    return td_list




# https://hr.tencent.com/position_detail.php?id=49099&keywords=python&tid=0&lid=0
####爬取每一层的详情页
def second_crawl(td_list,params,headers):
    for td in td_list:
        tt = str(td)
        href_re = '<a.*?href="(.*?)".*?>'
        href_list = re.findall(href_re, tt, re.S)
        # print(href_list)

        #### 写入文件
        with open('./tencent.txt','a',encoding='utf8') as fp:
            ####路由拼接
            for hrefs in href_list:
                url = f'https://hr.tencent.com/{hrefs}'
                # print(url)

                ####爬取岗位具体内容
                response = requests.get(url, params=params, headers=headers)
                req = response.text
                suop = BeautifulSoup(req, 'lxml')
                ta = suop.find_all(name='ul', attrs=['squareli'])
                # print(ta)

                result = str(ta)
                fp.write(result)
                fp.flush()
            fp.close()





if __name__=="__main__":
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    url = 'https://hr.tencent.com/position.php'

    for i in range(0,100,10):
        params = {
            'keywords': 'python',
            'start': i
        }
        url_list = first_cwawl(url, params, headers)

        second_crawl(url_list, params, headers)