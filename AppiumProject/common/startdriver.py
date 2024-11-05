from appium import webdriver
import os
import threading

from AppiumProject.common.operationConf import ReadYamlConfig
from AppiumProject.common.recordlog import logs


class StartDriver(object):
    '''获取终端驱动'''
    conf = ReadYamlConfig()
    instance = None
    instance_lock = threading.Lock()

    def get_driver(self):
        data = self.conf.get_yamlfile()
        driver = None
        try:
            capabs = {
                "platformName": data.get("platformName"),
                "platformVersion": str(data.get("platformVersion")),
                "deviceName": data.get("deviceName"),
                "app": os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', data.get("appname")),
                "appPackage": data.get("appPackage"),
                "appActivity": data.get("appActivity"),
                "noReset": data.get("noReset"),
                "automationName": data.get("automationName"),
                "newCommandTimeout": data.get("newCommandTimeout")
            }

            # Ensure all required capabilities are set
            for key in ["platformName", "platformVersion", "deviceName", "app", "appPackage", "appActivity",
                        "automationName"]:
                if capabs[key] is None:
                    logs.error(f"Configuration for '{key}' is missing or invalid!")
                    return None

            logs.info("start app...")
            try:
                driver = webdriver.Remote(f"http://{data['ip']}:{data['port']}/wd/hub", capabs)
            except Exception as e:
                logs.error("Appium服务未连接!", exc_info=True)
                exit()

            logs.info(f"连接Appium：http://{data['ip']}:{data['port']}/wd/hub")
            driver.implicitly_wait(5)
            return driver
        except Exception as e:
            logs.error("Appium服务未启动或设备devices未连接!", exc_info=True)
            exit()

    def close_devices(self):
        driver = self.get_driver()
        if driver:
            driver.close()
