import csv
import yaml

from AppiumProject.common.recordlog import logs
from AppiumProject.conf import setting


class ReadCsvData(object):
    def __init__(self, csvfile=None):
        if csvfile != None:
            self.csvfile = csvfile
        self.csvfile = setting.FILE_PATH['csvpath']

    def get_csv_data(self, line):
        try:
            with open(self.csvfile, 'r', encoding='utf-8-sig') as cf:
                data = csv.reader(cf)
                for index, items in enumerate(data, 1):  # 从索引1开始
                    if index == line:
                        logs.info("获取数据:%s" % items)
                        return items
        except Exception as e:
            logs.error(e)


class ReadYamlConfig(object):
    '''读取Yaml格式文件'''

    def __init__(self, yaml_file=None):
        if yaml_file != None:
            self.yaml_file = yaml_file
        else:
            self.yaml_file = setting.FILE_PATH['yamlfp']

    def get_yamlfile(self):
        with open(self.yaml_file, 'r', encoding='utf-8') as yf:
            data = yaml.load(yf, Loader=yaml.FullLoader)
        return data
