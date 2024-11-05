
import logging
import os
import time
from logging.handlers import RotatingFileHandler  # 按文件大小滚动备份
import datetime

from AppiumProject.conf import setting

log_path = setting.FILE_PATH['logfp']
if not os.path.exists(log_path): os.mkdir(log_path)
logfile_name = log_path + r"\test.{}.log".format(time.strftime('%Y%m%d'))


class RecordLogs(object):
    def __init__(self):
        self.handle_overdue_log()

    def handle_overdue_log(self):
        "处理过期日志文件,"
        nowTime = datetime.datetime.now()  # 获取系统当前时间
        todays = datetime.timedelta(days=-30)  # 日期偏移7天
        nows = (nowTime + todays).timestamp()  # 获取前一天的时间戳
        # 找到目录下的文件
        files = os.listdir(log_path)
        for file in files:
            if os.path.splitext(file)[1]:
                filepath = log_path + "\\" + file
                file_createtime = os.path.getctime(filepath)  # 获取文件创建时间,返回时间戳
                # dateArray = datetime.datetime.fromtimestamp(file_createtime) #标准时间格式
                # print(dateArray.strftime("%Y--%m--%d %H:%M:%S"))
                if file_createtime < nows:
                    os.remove(filepath)
                else:
                    continue

    def output_logging(self):
        "获取logger对象"
        logger = logging.getLogger(__name__)
        if not logger.handlers:
            logger.setLevel(setting.LOG_LEVEL)
            log_format = logging.Formatter(
                    '[%(asctime)s] [%(filename)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s')
            # 日志输出到指定文件，滚动备份日志
            fh = RotatingFileHandler(filename=logfile_name, mode='a', maxBytes=5242880,
                                     backupCount=7,
                                     encoding='utf-8')  # maxBytes:控制单个日志文件的大小，单位是字节,backupCount:用于控制日志文件的数量

            fh.setLevel(setting.LOG_LEVEL)
            fh.setFormatter(log_format)
            logger.addHandler(fh)  # 将相应的handler添加在logger对象中
            # 输出到控制台
            sh = logging.StreamHandler()
            sh.setLevel(setting.STREAM_LOG_LEVEL)
            sh.setFormatter(log_format)
            logger.addHandler(sh)
        return logger


apilog = RecordLogs()
logs = apilog.output_logging()
