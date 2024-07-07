from handle.ocr.ocr import recognize
from handle.fix.text_fix import filtrate
import time
from threading import current_thread


def _login(webdriver, url, account, password, wait, auto):
    """
    :param webdriver: 浏览器驱动
    :param account: 登录账号
    :param password: 登录密码
    :param wait: 登录成功/失败后等待页面刷新的时间
    :return: None
    """

    # 获取网址页面
    webdriver.get(url)

    # 定位元素
    captcha_image = webdriver.find_element('xpath', '//*[@id="yzmPic"]')  # 验证码图片
    username_input = webdriver.find_element('xpath', '//*[@id="yhm"]')  # 用户名输入框
    password_input = webdriver.find_element('xpath', '//*[@id="mm"]')  # 密码输入框
    captcha_input = webdriver.find_element('xpath', '//*[@id="yzm"]')  # 验证码输入框
    confirm_btn = webdriver.find_element('xpath', '//*[@id="dl"]')  # 确认按钮

    # 识别验证码图片中的文本
    text = recognize(captcha_image.screenshot_as_base64)  # 使用了屏幕截图功能

    # 文本筛选
    text = filtrate(text)

    # 操作元素
    username_input.send_keys(account)
    password_input.send_keys(password)
    captcha_input.send_keys(text)
    if not auto:
        input(f'[thread-{current_thread().name}]>>> 按下`Enter键`继续...')  # 选择是否全自动登录
    confirm_btn.click()

    # 等待页面刷新
    time.sleep(wait)


def login(webdriver, url: str, account: str, password: str, wait: int = 0.1, auto: bool = True):
    """
    :param webdriver: 浏览器驱动
    :param url: 登录网址
    :param account: 账号
    :param password: 密码
    :param wait: 等待时间
    :param auto: 登录成功/失败后等待页面刷新的时间
    :return: 尝试登录次数
    """
    # 记录登录次数
    num = 0

    # 进入登录循环
    while True:
        num += 1
        _login(webdriver, url, account, password, wait, auto)
        try:
            # 尝试获取"登录错误"弹框元素，如果没有该元素，会报错，也说明了登录成功
            element = webdriver.find_element('xpath', '//*[@id="tips"]/span')
        except:
            break
    return num
