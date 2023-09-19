import os
import requests
import yaml
import sys


class Testurl():
    def test_server_url(self):

        yaml_path=os.path.abspath('../TestDatas/check_url.yaml')
        with open(yaml_path,'r',encoding='utf-8') as f:
                cfg=f.read()
                data=yaml.safe_load(cfg)
                urls=data.get('URL',[])
                print('这是集合{}'.format(urls))
                if not urls:
                    return False
                status=[requests.get(url).status_code != 200 for url in urls]
                return all(status)
