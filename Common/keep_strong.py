# -*- coding:utf-8 -*-
# from ui.TestDatas.global_datas import GlobalDatas
import requests

import os
import yaml

class KeepStrong():

    def server_probing(self):
        """服务器探活操作"""
        # 获取yaml文件路径
        yamlPath = os.path.abspath("./TestDatas/check_url.yaml")
        with open(yamlPath,'r',encoding='utf-8') as f:
            cfg=f.read()
            data=yaml.safe_load(cfg)
            urls=data.get('URL',[])
            if not urls:
                return False
            status=[requests.get(url).status_code == 200 for url in urls]
            return all(status)



