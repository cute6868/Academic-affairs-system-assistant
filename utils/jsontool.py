import json


def get_json_data(file_path: str) -> dict:
    """
    获取json数据，并转换为python对象

    :param file_path: json文件的所在路径
    :return: python字典
    """

    with open(file_path, mode='r', encoding='utf-8') as file:
        data = json.load(file)
    return data
