from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for_appear(webdriver, method, path):
    # 1.等待元素出现
    # 每隔0.3s判断元素是否出现，0.3可以不设置，默认为0.5s轮询一次，最长12s，超时未出现则报错
    WebDriverWait(webdriver, 12, 0.3).until(EC.presence_of_element_located((method, path)))

    # 2.获取并返回元素
    return webdriver.find_element(method, path)
