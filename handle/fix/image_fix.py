# # ========================= 测试使用 =========================
# from functools import wraps
# import base64
# from io import BytesIO
# from PIL import Image
#
#
# # 装饰器
# def save(path1: str, path2: str):
#     def outer(func):
#         @wraps(func)
#         def inner(*args, **kwargs):
#             save_base64_image(*args, path1)
#             res = func(*args, **kwargs)
#             save_base64_image(*args, path2)
#             return res
#
#         return inner
#
#     return outer
#
#
# def save_base64_image(base64_image: str, path: str) -> None:
#     image_data = base64.b64decode(base64_image)
#     image = Image.open(BytesIO(image_data))
#     image.save(path)
#
#
# # ========================= 测试使用 =========================


# @save('降噪前.png', '降噪后.png')  # 测试使用
def denoising(base64_image: str) -> str:
    """
    图片降噪
    :param base64_image: base64编码方式的图片数据流
    :return: 降噪后的base64编码方式的图片数据流
    """

    return base64_image
