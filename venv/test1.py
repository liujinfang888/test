import requests
import pytest
import allure

# @allure.feature('第一次第一个测试用例')
# @allure.story("第一个测试用例")
# def test_chaxun_reg(self):
#     url="https://testbistrategic.leqee.com/bistrategic/proxy/jobcenter/controller/jobcenter/sysbi/SysbiReportController/getReport?jobCode=LEQEE_STRATEGIC_PACK_FAC_SCALE_INFO&type=data&sheetIndex=2&key=enable"
#     headers={
#               "Cookie":  "JSESSIONID = B4DF377686D6D2E8442E38EB8480943E"
#     }
#     data={
#           "activity_name": "测试统筹活动"
#         }
#     res=requests.post(url,json=data,headers=headers)
#     assert 200 == res.json()['code']
#     assert "查询BI报表成功" in res.json()['message']

# -*- coding: utf-8 -*-
# @Time    : 2019/3/12 11:46
# @Author  : zzt

class TestAllure():
    @allure.story("这里是第1个1级标签")
    def test_1(self):
        print("这是一个测试")