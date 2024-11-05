import unittest
import time
from common.semail import SendEmail
from conf import setting
from common import removefile
from conf.setting import FILE_TYPE

if __name__ == "__main__":
    # 清理屏幕截图文件
    removefile.removeFile(setting.FILE_PATH['screen_path'], FILE_TYPE.get('p'))

    # 加载测试用例
    load_case = unittest.defaultTestLoader.discover(setting.FILE_PATH['testcase_path'], 'test_1login.py')

    # 获取当前时间并生成报告文件名
    now = time.strftime("%Y%m%d%H%M%S")
    report_name = setting.FILE_PATH['report_path'] + "\%s_%s" % (now, "testReport.txt")

    # 运行测试并生成报告
    with open(report_name, 'w') as rf:
        runner = unittest.TextTestRunner(stream=rf, verbosity=2)
        runner.run(load_case)

    # 发送邮件（如果需要）
    # SendEmail().send_email(report_name)

    # 清理报告文件
    removefile.removereport(FILE_TYPE.get('h'))
