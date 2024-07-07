from handle.core.task_login import task
from .base import activate


def assisted_login(*args):
    # 激活任务
    activate(task, *args)
