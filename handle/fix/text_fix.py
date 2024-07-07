def filtrate(text: str) -> str:
    """
    文本筛选
    :param text: 要被筛选的文本
    :return: 筛选后的文本
    """

    # 如果文本不只是由数字和字母组成，就剔除数字和字母以外的符号
    if not text.isalnum():
        text = ''.join(c for c in text if c.isalnum())

    # 如果文本长度大于6，则保留后6位字符
    length = len(text)
    if length > 6:
        text = text[-6:-1:1]

    return text
