import pytest
import requests
import json

from resources.data.constant import get_url, get_cookie
from utils.load_data import yaml_load

errmsg = None


@pytest.mark.parametrize('data', yaml_load.load('./resources/data/project.yaml').values())
def test_01(data):
    gamma_url = get_url()
    gamma_cookie = get_cookie()

    payload = {"category": "CustomerProject",
               "tab": "intention_project_v1",
               "sort": {"create_time": "desc"},
               "page_num": 1,
               "page_size": 100,
               "cid": "",
               "query": {"name": json.dumps(data['project'], ensure_ascii=False)},
               "filter": {},
               "fetch_mode": "body"
               }
    json_str = json.dumps(payload)

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': gamma_cookie}

    response = requests.request("POST", gamma_url, headers=headers, data=json_str)
    result = json.loads(response.text)

    try:
        global errmsg
        errmsg = result['errmsg']
        print(data['project'] + '返回值中获取到的name：' + errmsg)
    except:
        pass
        print('直接通过')

    assert json.dumps(data['errmsg'], ensure_ascii=False) == '"' + result['errmsg'] + '"'


# test()

def test_02():
    print(errmsg)

# # 以pytest模式运行（默认运行“test”开头的用例）
# if __name__ == '__main__':
#     pytest.main(['-v', '-s'])
