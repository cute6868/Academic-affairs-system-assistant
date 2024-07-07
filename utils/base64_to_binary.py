import base64


def to_binary(image_base64: str) -> bytes:
    """
    将base64格式的图片转为二进制格式的图片

    :param image_base64: base64字符串图片数据
    :return: bytes二进制图片数据
    """

    # 移除数据URL的前缀（注意：不是所有的base64编码的图片字符串都会有前缀，这取决于我们是如何获取这个字符串的）

    if image_base64.startswith('data:image/png;base64,'):
        base64_image_data = image_base64.split(',')[1]

    elif image_base64.startswith('data:image/jpeg;base64,'):
        base64_image_data = image_base64.split(',')[1]

    else:
        base64_image_data = image_base64  # 假设字符串已经是纯净的base64数据

    binary_image_data = base64.b64decode(base64_image_data)  # 解码base64数据为二进制流
    return binary_image_data
