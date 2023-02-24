import pytest
import requests
import json

from resources.data.constant import get_url, get_cookie
from utils.load_data import yaml_load

# 初始化errmsg
errmsg = None


# 读取yaml中的值（调用yaml_load.py文件中的load函数，且传入路径参数'../data/project.yaml'）
@pytest.mark.parametrize('data', yaml_load.load('./resources/data/project.yaml').values())
# 函数要传入参数
def test_03(data):
    gamma_url = get_url()
    gamma_cookie = get_cookie()

    # json.dumps 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False
    #print("11111111111" + json.dumps(data, ensure_ascii=False))

    # "query":{"name":"南京项目"}
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
    # print(payload)
    json_str = json.dumps(payload)  # 将传入的字典形式的只转化为字符串形式（需要导入“json包”）

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': gamma_cookie}

    response = requests.request("POST", gamma_url, headers=headers, data=json_str)  # 需要导入“requests包”

    result = json.loads(response.text)
    #print('实际的errmsg：' + '"' + result['errmsg'] + '"')
    # print(result)
    resu = json.dumps(data['errmsg'], ensure_ascii=False)
    #print('期待的errmsg：' + resu)

    try:
        global errmsg
        # 对errmsg重新赋值（由于errmsg是全局变量，赋值后其他的测试用例，比如test_02就能拿到test_01中赋值后的errmsg的新值）
        errmsg = result['errmsg']
        print(data['project'] + '返回值中获取到的name：' + errmsg)
    except:
        pass
        print('直接通过')

    assert json.dumps(data['errmsg'], ensure_ascii=False) == '"' + result['errmsg'] + '"'


# #可以使用main函数执行以test开头的函数
# test()

def test_04():
    print('打印从 test_01 获取到的errmsg： ' + errmsg)

# # 以pytest模式运行（默认运行“test”开头的用例）
# if __name__ == '__main__':
#     # -v:显示更详细的信息，文件名，用例名等等
#     # -s:输入调试信息。如：打印信息等等
#     pytest.main(['-v', '-s'])  # 需要导入“pytest包”
