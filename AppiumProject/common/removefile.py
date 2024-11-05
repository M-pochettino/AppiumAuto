import os
import datetime

from AppiumProject.conf import setting


def removeFile(path, type):
    file = os.listdir(path)  # 将目录下文件放入列表
    for f in file:
        if os.path.splitext(f)[1] == type:
            file = path + '\\' + f
            os.remove(file)
        else:
            continue


def removereport(type):
    nowTime = datetime.datetime.now()  # 当前时间
    todays = datetime.timedelta(days=-1)  # 日期偏移1天
    redate = (nowTime + todays).timestamp()  # 前1天的时间戳
    file = os.listdir(setting.FILE_PATH['report_path'])  # 找到目录下的文件，存在list
    for i in file:
        if os.path.splitext(i)[1] == type:
            filePath = setting.FILE_PATH['report_path'] + "\\" + i
            filectime = os.path.getctime(filePath)  # 获取文件的创建时间
            if filectime <= redate:
                os.remove(filePath)
        else:
            continue
