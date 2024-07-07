from handle.core.task_inquiry_schedule import task
from .base import activate


def inquiry_schedule(*args):
    # 激活任务
    activate(task, *args)
