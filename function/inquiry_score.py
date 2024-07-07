from handle.core.task_inquiry_score import task
from .base import activate


def inquiry_score(*args):
    # 激活任务
    activate(task, *args)
