from selenium.common.exceptions import WebDriverException
import time


def blocking(webdriver):
    # 阻塞
    while True:
        try:
            webdriver.find_element('tag name', 'body')
        except WebDriverException:
            break
        time.sleep(0.1)
    webdriver.quit()
