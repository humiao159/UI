#!/usr/bin/python3
# -*- coding:UTF-8 -*-
import os
from Common.clear_cache import *
from Common.file_config import FileConfig
import pytest

# 判断缓存文件是否存在，删除历史结果数据
if os.path.exists("{}\.pytest_cache".format(FileConfig().base_dir)) or os.path.exists(
        "{}/.pytest_cache".format(FileConfig().base_dir)):
    delete_file(FileConfig().get_path(type="allure_report"), FileConfig().get_path(type="logs"),
                FileConfig().get_path(type="pytest_report"), FileConfig().get_path(type="screenshots"))

# 执行main文件
pytest.main(["-s", "-v", "-m", "sj", "--html=Outputs/pytest_report/pytest.html", "--alluredir=Outputs/allure_report",'-n','2'])

# 生成allure报告
if platform.system() == "Windows":
    command_1 = "cd {}".format(FileConfig().get_path(type="allure_report"))
    command_2 = "allure generate {0} -o lwpa_UI_Report --clean".format(FileConfig().get_path(type="allure_report"))
    os.system('{0}&&{1}'.format(command_1, command_2))
else:
    command_1 = "cd {}".format(FileConfig().get_path(type="allure_report"))
    command_2 = "allure generate {0} -o lwpa_UI_Report --clean".format(FileConfig().get_path(type="allure_report"))
    os.system('{0}&&{1}'.format(command_1, command_2))