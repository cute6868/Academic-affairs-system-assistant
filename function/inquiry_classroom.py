from handle.core.task_inquiry_classroom import task
from .base import activate


def inquiry_classroom(*args):
    # 激活任务
    activate(task, *args)
