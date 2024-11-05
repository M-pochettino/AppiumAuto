import os
import sys
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

LOG_LEVEL = logging.INFO  #文件
STREAM_LOG_LEVEL = logging.DEBUG  #控制台

FILE_PATH = {
    'yamlfp': os.path.join(BASE_DIR, 'conf', 'devicesInfo.yaml'),
    'logfp': os.path.join(BASE_DIR, 'log'),
    'screen_path': os.path.join(BASE_DIR, 'screenshots'),
    'csvpath': os.path.join(BASE_DIR, 'data', 'account.csv'),
    'config_path': os.path.join(BASE_DIR, 'conf', 'config.ini'),
    'report_path': os.path.join(BASE_DIR, 'report'),
    'testcase_path': os.path.join(BASE_DIR, 'test_case'),
    'attach_path': os.path.join(BASE_DIR, 'report'),  # 邮件附件
    'appiumfp': os.path.join(BASE_DIR, 'log', 'appium_log')
}
FILE_TYPE = {
    'p': '.png',
    'j': '.jpg',
    'h': '.html',
    'b': '.bmp'
}


