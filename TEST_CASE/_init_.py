import requests

class TestClass(object):
    base_url = "https://testbistrategic.leqee.com"
    def __init__(self,url):
        self.url=self.base_url+url

    def chaxun_reg(self,activity_name):
        url="/bistrategic/proxy/jobcenter/controller/jobcenter/sysbi/SysbiReportController/getReport?jobCode=LEQEE_STRATEGIC_PACK_FAC_SCALE_INFO&type=data&sheetIndex=2&key=enable"
        headers={
              "Cookie":  "JSESSIONID = B4DF377686D6D2E8442E38EB8480943E"
        }
        params={
          "activity_name": activity_name
        }
        res=requests.post(url,json=params,headers=headers)
        # assert 200 == res.json()['code']
        # assert "查询BI报表成功" in res.json()['message']
