from datetime import datetime
import time


def wait_until(year: int = -1, month: int = -1, day: int = -1, hour: int = -1, minute: int = -1, second: int = -1,
               microsecond: int = -1) -> None:
    """
    默认值为-1：采用当前的日期/时间

    :param year: 等待时刻所在的年分
    :param month: 等待时刻所在的月份
    :param day: 等待时刻所在的天
    :param hour: 等待时刻所在的小时
    :param minute: 等待时刻所在的分钟
    :param second: 等待时刻所在的秒数
    :param microsecond: 等待时刻所在的毫秒数
    :return: None
    """

    now = datetime.now()
    if year == -1:
        year = now.year
    if month == -1:
        month = now.month
    if day == -1:
        day = now.day
    if hour == -1:
        hour = now.hour
    if minute == -1:
        minute = now.minute
    if second == -1:
        second = now.second
    if microsecond == -1:
        microsecond = now.microsecond
    future = datetime(year, month, day, hour, minute, second, microsecond)
    delta = (future - now).total_seconds()
    if delta < 0:
        raise Exception('请不要设置过去的时间')
    time.sleep(delta)
