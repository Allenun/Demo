import yaml


# 新建函数读取yaml文件（yaml格式内容的数据读取）
def load(path):
    file = open(path, 'r', encoding='utf-8')  # 打开文件
    data = yaml.load(file, Loader=yaml.FullLoader)  # 读取数据
    #print(data)
    return data


# 调用方法1:调取新建的函数，且传入文件读取路径

# load('../../resources/data/project.yaml')
