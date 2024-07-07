from threading import Thread


def multi_thread(who: list, task,
                 year: int, month: int, day: int,
                 hour: int, minute: int, second: int,
                 microsecond: int):
    # 存放线程对象
    thread_list = []

    # 创建所有线程
    for p in who:
        t = Thread(
            target=task,  # 线程要执行的函数
            name=p.name,  # 线程的名字
            args=(p, year, month, day, hour, minute, second, microsecond)  # 被执行函数所需要的参数
        )
        thread_list.append(t)

    # 执行所有线程
    for t in thread_list:
        t.start()

    # 等待所有线程执行完毕
    for t in thread_list:
        t.join()
