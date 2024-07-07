import tkinter as tk
from tkinter import messagebox
from utils import get_json_data, is_url, contains_chinese
from handle import multi_thread


def show_message(title, message):
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    messagebox.showinfo(title, message)
    root.destroy()  # 销毁窗口


class People:
    def __init__(self, name, auto, url, account, password):
        self.name = name
        self.auto = auto
        self.url = url
        self.account = account
        self.password = password


def activate(task, *args):
    # 1. 从本地文件中解析json数据
    data = get_json_data('./res/data.json')

    # 2. 获取操作对象的信息
    objs = []
    for key, value in data.items():
        if value.get('switch') == 'True':
            obj = People(key, value.get('auto-login'), value.get('url'), value.get('account'), value.get('password'))
            objs.append(obj)

    # 3. 用户数据合法性检验
    for obj in objs:
        legal = is_url(obj.url) and obj.account.isalnum() and (not contains_chinese(obj.password))
        if not legal:
            show_message('温馨提示', f'内容或格式错误！请检查{obj.name}的信息。')
            return None

    # 3. 让所有的对象执行各自的任务
    year, month, day, hour, minute, second = args[1]
    multi_thread(objs, task,
                 int(year.get()), int(month.get()), int(day.get()),
                 int(hour.get()), int(minute.get()), int(second.get()),
                 -1)
