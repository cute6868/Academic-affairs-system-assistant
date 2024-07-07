import re


def is_url(string):
    """
    这个函数检查给定的字符串是否是一个有效的URL。

    :param string: 要检查的输入字符串
    :return: bool，如果字符串是有效的URL，则为True，否则为False
    """

    url_pattern = re.compile(
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    )

    match = url_pattern.match(string)

    return bool(match)


def contains_chinese(string):
    """
    判断给定字符串是否包含中文字符。

    :param string: str, 要检查的输入字符串
    :return: bool, 如果字符串至少包含一个中文字符，则返回True，否则返回False
    """
    # 使用正则表达式匹配中文字符的模式
    chinese_pattern = re.compile(r'[\u4e00-\u9fff]+')

    # 在字符串中搜索中文字符模式的匹配项
    match = chinese_pattern.search(string)

    # 如果找到匹配项，则返回True，否则返回False
    return bool(match)
