from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

from AppiumProject.common.commonfunc import CommonFunction


class LoginPage(CommonFunction):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def swipe_to_bottom(self):
        # 获取屏幕的尺寸
        screen_size = self.driver.get_window_size()
        width = screen_size['width']
        height = screen_size['height']

        # 计算滑动起始和终止的坐标
        start_x = width / 2
        start_y = height * 0.8
        end_x = start_x
        end_y = height * 0.2

        # 记录上一次页面的源代码
        last_page_source = None

        while True:
            # 获取当前页面的源代码
            current_page_source = self.driver.page_source

            # 如果当前页面源代码与上一次相同，说明已经滑动到底部
            if current_page_source == last_page_source:
                print("Reached the bottom of the page.")
                break

            # 更新上一次页面的源代码
            last_page_source = current_page_source

            # 使用TouchAction进行滑动
            action = TouchAction(self.driver)
            action.press(x=start_x, y=start_y).wait(1000).move_to(x=end_x, y=end_y).release().perform()

            # 等待页面加载
            time.sleep(1)

        print("Swiped to the bottom of the page successfully.")

    def loginView(self):
        try:
            # 定位并点击ImageView元素
            element1 = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    "//android.widget.ImageView[contains(@content-desc, '我的第4个标签')]"
                ))
            )
            element1.click()
            print("Element clicked successfully.")

            # 定位并点击Button元素
            button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    "//android.widget.Button[@index='2' and @content-desc='登录/注册']"
                ))
            )
            button.click()
            print("Button clicked successfully.")

            # 使用XPath定位content-desc为“手机登录”的View元素
            view_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    "//android.view.View[@content-desc='手机登录']"
                ))
            )
            # 点击该元素
            view_element.click()
            print("View element with content-desc '手机登录' clicked successfully.")

            # # 定位EditText元素并输入手机号
            # email_input = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((
            #         By.XPATH,
            #         "//android.widget.EditText[@index='6']"
            #     ))
            # )
            # self.input_if_empty(email_input, "17625764003")
            #
            # # 定位EditText元素并输入密码
            # password_input = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((
            #         By.XPATH,
            #         "//android.widget.EditText[@index='7']"
            #     ))
            # )
            # self.input_if_empty(password_input, "hlhlhl123")

            # # 定位ImageView元素并点击
            # remember_password = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((
            #         By.XPATH,
            #         "//android.widget.ImageView[@index='8' and @content-desc='记住密码']"
            #     ))
            # )
            # if not remember_password.is_selected():
            #     remember_password.click()
            # print("Remember password ImageView clicked successfully.")

            # 定位立即登录按钮并点击
            login_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    "//android.widget.Button[@content-desc='立即登录']"
                ))
            )
            login_button.click()
            print("Login button clicked successfully.")

            # 定位“同意”按钮并点击
            agree_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    "//android.widget.Button[@index='2' and @content-desc='同意']"
                ))
            )
            agree_button.click()
            print("Agree button clicked successfully.")

            # # 使用XPath定位包含“购买”的ImageView元素
            # image_view = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((
            #         By.XPATH,
            #         "//android.widget.ImageView[contains(@content-desc, '购买') and @index='2']"
            #     ))
            # )
            # # 点击该元素
            # image_view.click()
            # print("ImageView with '购买' clicked successfully.")
            #
            # # 使用XPath定位text为“SVIP会员”的View元素
            # view_element = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((
            #         By.XPATH,
            #         "//android.view.View[@text='SVIP会员']"
            #     ))
            # )
            # # 点击该元素
            # view_element.click()
            # print("View with text 'SVIP会员' clicked successfully.")
            #
            # # 使用XPath定位content-desc包含“加速”的ImageView元素
            # image_view_element = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((
            #         By.XPATH,
            #         "//android.widget.ImageView[contains(@content-desc, '加速')]"
            #     ))
            # )
            # # 点击该元素
            # image_view_element.click()
            # print("ImageView with content-desc containing '加速' clicked successfully.")
            #
            # # 使用XPath定位content-desc包含“影音加速”的View元素
            # view_element = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((
            #         By.XPATH,
            #         "//android.view.View[contains(@content-desc, '影音加速')]"
            #     ))
            # )
            # # 点击该元素
            # view_element.click()
            # print("View with content-desc containing '影音加速' clicked successfully.")
            #
            # # 使用XPath定位content-desc包含“游戏加速”的View元素
            # view_element = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((
            #         By.XPATH,
            #         "//android.view.View[contains(@content-desc, '游戏加速')]"
            #     ))
            # )
            # # 点击该元素
            # view_element.click()
            # print("View with content-desc containing '游戏加速' clicked successfully.")
            #
            # self.swipe_to_bottom()
            #
            # # 使用XPath定位包含“立即添加”的ImageView元素
            # image_view = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((
            #         By.XPATH,
            #         "//android.widget.ImageView[contains(@content-desc, '立即添加')]"
            #     ))
            # )
            # # 点击该元素
            # image_view.click()
            # print("ImageView with '立即添加' clicked successfully.")
            #
            # # 使用XPath定位content-desc为“取消”的Button元素
            # button_element = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((
            #         By.XPATH,
            #         "//android.widget.Button[@content-desc='取消']"
            #     ))
            # )
            # # 点击该元素
            # button_element.click()
            # print("Button with content-desc '取消' clicked successfully.")
            #
            # 使用XPath定位包含“积分”的ImageView元素
            image_view = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    "//android.widget.ImageView[contains(@content-desc, '积分')]"
                ))
            )
            # 点击该元素
            image_view.click()
            print("ImageView with points clicked successfully.")

            # 使用XPath定位“邀请好友”的TextView元素
            text_view = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    "//android.widget.TextView[@text='邀请好友' and @index='0']"
                ))
            )
            # 点击该元素
            text_view.click()
            print("TextView with '积分记录' clicked successfully.")

            time.sleep(2)

            # # 使用XPath定位text为“赚佣金”的View元素
            # view_element = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((
            #         By.XPATH,
            #         "//android.view.View[@text='赚佣金']"
            #     ))
            # )
            # # 点击该元素
            # view_element.click()
            # print("View with text '赚佣金' clicked successfully.")
            #
            # # 使用XPath定位text为“联系客服”的Button元素
            # button_element = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((
            #         By.XPATH,
            #         "//android.widget.Button[@text='联系客服']"
            #     ))
            # )
            # # 点击该元素
            # button_element.click()
            # print("Button with text '联系客服' clicked successfully.")
            #
            # # 使用XPath定位index为2的EditText元素
            # edit_text_element = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((
            #         By.XPATH,
            #         "//android.widget.EditText[@index='2']"
            #     ))
            # )
            # # 点击该元素
            # edit_text_element.click()
            # # 输入文本“一个大问题”
            # edit_text_element.send_keys("一个大问题")
            # print("Text '一个大问题' entered successfully in EditText at index 2.")
            #
            # # 使用XPath定位index为2的EditText元素
            # edit_text_element = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((
            #         By.XPATH,
            #         "//android.widget.EditText[@index='4']"
            #     ))
            # )
            # # 点击该元素
            # edit_text_element.click()
            # # 输入文本“一个大问题”
            # edit_text_element.send_keys("18554854741")
            # print("Text '联系方式' entered successfully in EditText at index 2.")
            #
            # # 使用XPath定位content-desc为“确认”的Button元素
            # button_element = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((
            #         By.XPATH,
            #         "//android.widget.Button[@content-desc='确认']"
            #     ))
            # )
            # # 点击该元素
            # button_element.click()
            # print("Button with content-desc '确认' clicked successfully.")
            #
            # # 使用XPath定位content-desc为“确定”的Button元素
            # button_element = WebDriverWait(self.driver, 10).until(
            #     EC.presence_of_element_located((
            #         By.XPATH,
            #         "//android.widget.Button[@content-desc='确定']"
            #     ))
            # )
            # # 点击该元素
            # button_element.click()
            # print("Button with content-desc '确定' clicked successfully.")

            # 使用XPath定位bounds为"[44,148][90,196]"的View元素
            view_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    "//android.view.View[@bounds='[44,148][90,196]']"
                ))
            )
            # 点击该元素
            view_element.click()
            print("View with bounds '[44,148][90,196]' clicked successfully.")

            for _ in range(10):  # 循环执行10次
                # 使用XPath定位具有特定文本的"立即签到"按钮
                button_sign_in = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.XPATH,
                        "//android.widget.Button[@text='立即签到']"
                    ))
                )

                # 点击"立即签到"按钮
                button_sign_in.click()
                print("Button with text '立即签到' clicked successfully.")

                # 检查是否弹出 Dialog
                try:
                    dialog = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((
                            By.CLASS_NAME,
                            "android.app.Dialog"
                        ))
                    )
                    print("Dialog appeared after clicking '立即签到'.")
                except:
                    # 如果没有出现 Dialog，再次点击"立即签到"
                    print("Dialog did not appear. Retrying '立即签到' click.")
                    continue  # 继续下一个循环，重新尝试点击

                # 使用XPath定位具有特定文本的"开心收下"按钮
                button_accept = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.XPATH,
                        "//android.widget.Button[@text='开心收下']"
                    ))
                )

                # 点击"开心收下"按钮
                button_accept.click()
                print("Button with text '开心收下' clicked successfully.")

                # 可选：在每次循环之间等待一段时间
                time.sleep(1)

            # 获取屏幕的尺寸
            screen_size = self.driver.get_window_size()
            width = screen_size['width']
            height = screen_size['height']

            # 计算滑动起始和终止的坐标
            start_x = width / 2
            start_y = height * 0.8
            end_x = start_x
            end_y = height * 0.4

            # 使用TouchAction进行滑动
            action = TouchAction(self.driver)
            action.press(x=start_x, y=start_y).wait(1000).move_to(x=end_x, y=end_y).release().perform()
            print("Page swiped successfully.")

            # 使用XPath定位“1天SVIP会员”的TextView元素
            text_view = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    "//android.widget.TextView[@text='300']"
                ))
            )
            # 点击该元素
            text_view.click()
            print("TextView with '300' clicked successfully.")

            time.sleep(1)

            # 使用XPath定位text为“立即兑换”的Button元素
            button_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    "//android.widget.Button[@text='立即兑换']"
                ))
            )
            # 点击该元素
            button_element.click()
            print("Button with text '立即兑换' clicked successfully.")

            # 使用XPath定位content-desc包含“时长直接充值到当前账号”的View元素
            view_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    "//android.view.View[(@text='时长直接充值到当前账号')]"
                ))
            )
            # 点击该元素
            view_element.click()
            print("View with content-desc containing '时长直接充值到当前账号' clicked successfully.")

            # 使用XPath定位text为“去查看”的Button元素
            button_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((
                    By.XPATH,
                    "//android.widget.Button[@text='去查看']"
                ))
            )
            # 点击该元素
            button_element.click()
            print("Button with text '去查看' clicked successfully.")

        except Exception as e:
            print(f"An error occurred: {e}")
