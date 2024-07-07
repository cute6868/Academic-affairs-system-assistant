from .baidu_ocr import ocr
from handle.fix import denoising
from utils.base64_to_binary import to_binary


def recognize(base64_image: str) -> str:
    """
    图像文本识别
    :param base64_image: base64编码方式的图片数据流
    :return: 图片中文本
    """

    # 图片降噪
    base64_image = denoising(base64_image)

    # 识别图片
    binary_image = to_binary(base64_image)  # 将base64编码方式的图片转为二进制格式（str->bytes）
    data = ocr(binary_image)

    # 返回文本
    return data.text
