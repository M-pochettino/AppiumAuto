
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By  # ***元素定位***
import time

from AppiumProject.base.baseView import BaseView
from AppiumProject.common.recordlog import logs
from AppiumProject.conf import setting


class CommonFunction(BaseView):
    '''公共方法，继承Baseview'''

    btn_enter = (By.ID, "com.sxhsh:id/guide_login")
    skip_btn = (By.ID, "com.sxhsh:id/splash_tv_jump")
    close_btn = (By.ID, "com.sxhsh:id/popup_advert_close_btn")
    checkbox = (By.ID, "com.sxhsh:id/checkbox")  # 温馨提示同意
    agreed_btn = (By.ID, "com.sxhsh:id/submit_btn")  # 同意按钮
    ibtn = (By.ID, "com.sxhsh:id/tab5_ll")  # 我模块
    comBtn = (By.ID, "com.sxhsh:id/tab1_ll")  # 通信
    setting_btn = (By.ID, "com.sxhsh:id/ll_setting")  # 设置
    logout_btn = (By.XPATH, "//android.widget.TextView[@text='退出登录']")
    button_left = (By.ID, "com.sxhsh:id/button_left")  # 弹框，确定
    BACK_BTN = (By.ID, "com.sxhsh:id/iv_toolbar_back_icon")  # 页面返回按钮

    # 获取屏幕滑动尺寸
    def get_size(self):
        try:
            x = self.get_window_size()["width"]  # x值为720，其实就是屏幕分辨率
            y = self.get_window_size()["height"]  # y值为1280,返回一个元组(720,1280)
            return x, y
        except Exception as e:
            logs.error("Failed to get screen size")

    # 检测app启动弹出广告页
    def skip_page(self):
        try:
            skip_element = self.driver.find_element(*self.skip_btn)
        except NoSuchElementException:
            pass
        else:
            skip_element.click()

    # 检查登录成功后通信首页广告弹框
    def check_bounced(self):
        try:
            clo_element = self.driver.find_element(*self.close_btn)
        except NoSuchElementException:
            pass
        else:
            clo_element.click()

    # 向右滑
    def swipeRight(self):
        lef = self.get_size()
        x1 = int(lef[0] * 0.9)
        y1 = int(lef[1] * 0.5)
        x2 = int(lef[0] * 0.1)
        self.get_swipe(x1, y1, x2, y1, 1000)

    def swipeLeft(self):
        """向左滑，从屏幕的右端点击一个坐标点往左滑动到另外一个坐标点。
        Y坐标可以不改变。X的开始和结束坐标改变即可。"""
        try:
            rig = self.get_size()
            x1 = int(rig[0] * 0.99)
            y1 = int(rig[1] * 0.99)
            x2 = int(rig[0] * 0.15)
            s = 0
            time.sleep(2)
            while s < 4:
                self.get_swipe(x1, y1, x2, x1, 1000)
                s += 1
        except Exception as e:
            logs.error("引导页滑动失败!")

    def swipeDecline(self):
        """向下滑动，从屏幕的上端点击一个坐标然后往下滑动到另外一个坐标，
        x坐标可以不变。Y的开始和结束坐标改变即可"""
        time.sleep(2)
        left = self.get_size()
        start_x = int(left[0] * 0.5)  # 360
        start_y = int(left[1] * 0.25)  # 320
        end_x = int(left[0] * 0.5)
        end_y = int(left[1] * 0.75)  # 960
        self.get_swipe(start_x, start_y, end_x, end_y, 2000)

    def swipeSlide(self, t):
        """向上滑动，从屏幕的下端点击一个坐标然后往上滑动，
        x坐标可以不变。Y的开始和结束坐标改进即可。"""
        time.sleep(2)
        left = self.get_size()
        start_x = int(left[0] * 0.5)  # 360
        start_y = int(left[1] * 0.75)  # 960
        end_x = int(left[0] * 0.5)
        end_y = int(left[1] * 0.16)  # 256
        self.get_swipe(start_x, start_y, end_x, end_y, t)

    # 截图
    def getScreenshot(self, module):
        nowTime = time.strftime("%Y-%m-%d %H_%M_%S")
        image_file = '%s/%s_%s.png' % (setting.FILE_PATH['screen_path'], module, nowTime)
        # logs.info("get %s screenshot"%module)
        self.driver.get_screenshot_as_file(image_file)

    def screenshot(self):
        import os
        imageName = time.strftime("%Y-%m-%d %H_%M_%S") + '.png'
        imagepath = '//sdcard//' + imageName  # 手机路径
        path = setting.FILE_PATH['screen_path']  # 本地保存路径
        if not os.path.exists(path):
            os.mkdir(path)
        os.system("adb shell //system//bin//screencap -p " + imagepath)
        os.system('adb pull' + imagepath + path)
        screenshotUrl = path + "\\" + imageName

        # 滑动引导页，然后立即进入

    def enter_butn(self):
        try:
            self.swipeLeft()
        except NoSuchElementException:
            logs.error("启动失败!")
        else:
            self.find_element(*self.btn_enter).click()

    # 退出登录
    def logoutView(self):
        try:
            self.driver.find_element(*self.ibtn).click()
        except NoSuchElementException:
            pass
        else:
            self.driver.find_element(*self.setting_btn).click()
            self.driver.find_element(*self.logout_btn).click()
            self.driver.find_element(*self.button_left).click()
            logs.info("logout success!")

    # 温馨提示
    def click_Warmprompt(self):
        try:
            checkBox = self.driver.find_element(*self.checkbox)
        except NoSuchElementException:
            self.logoutView()
        else:
            checkBox.click()
            self.driver.find_element(*self.agreed_btn).click()
