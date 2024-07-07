from selenium.webdriver import Edge
from utils import wait_until
from .login import login
from .wait_for_appear import wait_for_appear
from .block import blocking


def task(people, year, month, day, hour, minute, second, microsecond):
    # 获取浏览器驱动（打开浏览器）
    driver = Edge()

    # 等待任务开始
    wait_until(year, month, day, hour, minute, second, microsecond)

    # 进行登录
    login(driver, people.url, people.account, people.password, auto=people.auto)

    # 查询分数
    wait_for_appear(driver, 'css selector',
                    '#cdNav > ul > li:nth-child(4)').click()
    wait_for_appear(driver, 'css selector',
                    '#cdNav > ul > li.dropdown.open > ul > li:nth-child(9)').click()

    # 阻塞
    blocking(driver)
