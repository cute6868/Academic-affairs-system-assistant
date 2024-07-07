# tkinter技术文档：https://blog.csdn.net/xufive/article/details/124514094
# tkinter布局文档：https://blog.csdn.net/superfanstoprogram/article/details/83713196
# 字体跟随窗口变化：https://cloud.tencent.com/developer/ask/sof/104257396


import functools
from tkinter import *
from function import maps
from datetime import datetime, timedelta
from utils import get_json_data


class App(Tk):

    def __init__(self):
        """初始化窗口"""

        super().__init__()
        self.title('教务系统助手')
        self.geometry('800x500')
        self.resizable(False, False)  # 防止用户调整尺寸
        self.iconbitmap('./res/imgs/cute.ico')
        self.init_ui()

    def init_ui(self):
        """初始化界面"""
        # pack()默认参数：xxx.pack(side='top', anchor='center', expand='no', fill='none', padx=0, pady=0)

        # ------ 底层框架 ------
        base_frame = Frame(self, bg='#90C0C0')
        base_frame.pack(side='top', expand=True, fill='both', padx=5, pady=5)

        # ------ 左边框架 ------
        left_frame = Frame(base_frame)
        left_frame.pack(side='left', fill='both', padx=10, pady=10)

        # ------ 右边框架 ------
        right_frame = Frame(base_frame)
        right_frame.pack(side='right', fill='both', padx=10, pady=10)

        # ------ 左边框架的顶部框架 ------
        top_frame = Frame(left_frame)
        top_frame.pack(side='top', fill='x', padx=10, pady=10)

        # ------ 时间输入框区 ------
        year, month, day, hour, minute, second = StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()
        time = (year, month, day, hour, minute, second)
        # 年
        Entry(top_frame, textvariable=year, width=5, justify='center').pack(side='left', pady=5)
        Label(top_frame, text='年 ').pack(side='left', pady=5)
        # 月
        Entry(top_frame, textvariable=month, width=5, justify='center').pack(side='left', pady=5)
        Label(top_frame, text='月 ').pack(side='left', pady=5)
        # 日
        Entry(top_frame, textvariable=day, width=5, justify='center').pack(side='left', pady=5)
        Label(top_frame, text='日 ').pack(side='left', pady=5)
        # 时
        Entry(top_frame, textvariable=hour, width=5, justify='center').pack(side='left', pady=5)
        Label(top_frame, text='时 ').pack(side='left', pady=5)
        # 分
        Entry(top_frame, textvariable=minute, width=5, justify='center').pack(side='left', pady=5)
        Label(top_frame, text='分 ').pack(side='left', pady=5)
        # 秒
        Entry(top_frame, textvariable=second, width=5, justify='center').pack(side='left', pady=5)
        Label(top_frame, text='秒 ').pack(side='left', pady=5)

        # 延时区域
        delay = StringVar()
        delay.set(get_json_data('./res/system.json').get('Delay'))  # 默认延时秒数
        Label(top_frame, text='秒').pack(side='right', pady=5)
        Entry(top_frame, textvariable=delay, width=8, justify='center').pack(side='right', pady=5)

        def set_time():
            # 1.获取当前时间
            now = datetime.now()
            # 2.计算延时
            now += timedelta(seconds=int(delay.get()))
            # 3.填入时间
            year.set(str(now.year))
            month.set(str(now.month))
            day.set(str(now.day))
            hour.set(str(now.hour))
            minute.set(str(now.minute))
            second.set(str(now.second))

        # 延时按钮
        Button(top_frame, text='从此刻延时', width=14, command=set_time).pack(side='right', padx='5')

        # ------ 文本区 ------
        text = Text(left_frame, wrap='word', font=("Arial", 10), width=90, height=28)
        text.pack(side='top', expand=True)

        # ------ 按钮区 ------
        for name, func in maps.items():
            btn = Button(right_frame, text=name, width=10)
            btn.configure(command=functools.partial(func, text, time))
            btn.pack(padx=5, pady=5)

    def run(self):
        self.mainloop()

    def close(self):
        self.destroy()
