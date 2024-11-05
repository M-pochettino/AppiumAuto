import unittest, time

from AppiumProject.common.recordlog import logs
from AppiumProject.common.startdriver import StartDriver


# from common.commonfunc import CommonFunction

class UnittestFunc(unittest.TestCase):
    def setUp(self):  # 每个case运行之前先运行此方法
        # logs.info("=====setUp=====")
        # self.imgs = []
        self.stdri = StartDriver()
        self.driver = self.stdri.get_driver()
        # com = CommonFunction(self.driver)
        # com.skip_page()
        # com.check_bounced()
        logs.info("正在执行测试用例...")

    def tearDown(self):
        # logs.info("=====tearDown=====")
        # time.sleep(1)
        # self.driver.close_app()
        self.driver.quit()
