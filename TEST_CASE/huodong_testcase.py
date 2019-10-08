import pytest
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from all_api.huodong import HuoDong
@pytest.mark.parametrize("activity_name,shop_id",[("测试统筹活动",18),("测试普通活动整体预估",1)])
def test_huodong_jiaoyan_chaxun(activity_name,shop_id):
    url = "/bistrategic/proxy/jobcenter/controller/jobcenter/sysbi/SysbiReportController/getReport?type=data&jobCode=STRATEGIC_ACTIVITIES_QUERY&sheetIndex=1&sqlKey=center&key=enable"
    huodong=HuoDong(url)
    res=huodong.chaxun_reg(activity_name,shop_id)
    assert 200 == res.json()['code']
    assert "查询BI报表成功" in res.json()['message']