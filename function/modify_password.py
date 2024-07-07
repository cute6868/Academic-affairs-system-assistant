from handle.core.task_modify_password import task
from .base import activate


def modify_password(*args):
    # 激活任务
    activate(task, *args)
