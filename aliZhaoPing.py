# -*- coding:utf-8 -*-
import json
import urllib.request
import urllib
from urllib import parse


# url = 'https://job.alibaba.com/zhaopin/socialPositionList/doList.json'
# data = {
#     'pageIndex': 1,
#     'keyWord': 'python',
# }


# 爬取阿里招聘
def alibaba(url, data):
    # for i in range(1,6):
    #     data0 = {
    #         'pageIndex': i,
    #         'keyWord': 'python',
    #     }
    #
    #     data = urllib.parse.urlencode(data0).encode("utf-8")

    headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

    res = urllib.request.Request(url=url, data=data, headers=headers)
    response = urllib.request.urlopen(res)
    content = response.read().decode()
    # print(content)
    return content


# 提取学历、部门、岗位要求、工作经验
def params(content,k=0):
    data1 = json.loads(content)
    datas = data1.get('returnValue')
    data_list = datas.get('datas')

    #写入文件
    with open('./ali.txt', 'a',encoding='utf-8') as fp:
        dis = []

        # 遍历
        for works in data_list:
            # print(works)
            degree = works['degree']
            departmentName = works['departmentName']
            workExperience = works['workExperience']
            requirement = works['requirement']

            k +=1
            # print(k,f'学历: {degree}, 部门：{departmentName}, 工作经验：{workExperience}, 要求：{requirement}')
            haha = (k,f'学历: {degree}, 部门：{departmentName}, 工作经验：{workExperience}, 要求：{requirement}')
            dis.append(haha)
        fp.write(str(dis))
        fp.flush()
    fp.close()

if __name__=='__main__':

    # pageSize: 10
    # t: 0.844015693927159
    # keyWord: python
    # location: 深圳
    # pageIndex: 1

    for i in range(1,11):
        data0 = {
            'pageSize': 10,
            't': 0.844015693927159,
            'pageIndex': i,
            'keyWord': 'python',
            'location': '深圳'
        }

        url = 'https://job.alibaba.com/zhaopin/socialPositionList/doList.json'
        data = urllib.parse.urlencode(data0).encode("utf-8")

        content = alibaba(url,data)
        params(content)


