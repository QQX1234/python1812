


# 作业1 : 分页获取豆瓣的数据（json数据）， 把电影图片存入本地，且图片名取电影名
# url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start="+ str(i * 20)+"&limit=20"



from urllib import request
import json


def get_data(i):

    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

    url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start="+ str(i * 20)+"&limit=20"

    req = request.Request(url, headers=headers)
    response = request.urlopen(req)
    content = response.read().decode()
    movie_list = json.loads(content)

    for movie in movie_list:
        cover_url = movie.get('cover_url')
        title = movie.get('title')

        request.urlretrieve(cover_url, './images1/%s.png'%title)
        request.urlcleanup()


if __name__ == '__main__':
    for i in range(5):
        get_data(i)












