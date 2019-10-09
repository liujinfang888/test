import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
#
# # 2.定义：取最新测试报告
# def new_file(test_dir):
#     # 列举test_dir目录下的所有文件，结果以列表形式返回。
#     lists = os.listdir(test_dir)
#     # sort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
#     # 最后对lists元素，按文件修改时间大小从小到大排序。
#     lists.sort(key=lambda fn: os.path.getmtime(test_dir + '\\' + fn))
#     # 获取最新文件的绝对路径
#     file_path = os.path.join(test_dir, lists[-1])
#     return file_path

def send_email(newfile):
    mail_title = '主题：测试报告'
    sender = '1263878183@qq.com'
    receiver = 'jfliu@leqee.com'
    smtpserver = 'smtp.qq.com'
    username = '1263878183'
    password = 'lcpppuzaxiouhjbg'
    # 读取html文件内容
    f = open(newfile ,'rb')
    mail_body = f.read()
    f.close()
    # 邮件内容, 格式, 编码
    message = MIMEText(mail_body, 'html', 'utf-8')
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = Header(mail_title, 'utf-8')
    try:
        smtp = smtplib.SMTP_SSL()
        smtp.connect('smtp.qq.com',465)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, message.as_string())
        print("发送邮件成功！！！")
        smtp.quit()
    except smtplib.SMTPException:
        print("发送邮件失败！！！")


if __name__ == '__main__':
    # cmd = "py.test test.py --html=./reports/test6.html"
    # os.system(cmd)
    # test_dir = 'F:\\untitled1\\venv'
    # 知道测试报告的路径
    # test_report_dir = 'F:/untitled1/TEST_CASE/report'
    now = time.strftime('%Y-%m-%d_%H_%M_%S_')
    filename = 'F:/untitled1/TEST_CASE/report/result.html'
    # fp = open(filename, 'wb')
    # #runner = HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况：')
    # #runner.run(discover)
    # fp.close()
    # new_report = new_file(test_report_dir)
    send_email(filename)

