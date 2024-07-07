from .load_data import load_data
from .save_data import save_data
from .assisted_login import assisted_login
from .inquiry_score import inquiry_score
from .inquiry_classroom import inquiry_classroom
from .inquiry_schedule import inquiry_schedule
from .modify_password import modify_password


def test(text):
    pass


maps = {
    '刷新页面': load_data,
    '保存数据': save_data,
    '协助登录': assisted_login,
    '查询成绩': inquiry_score,
    '查询空课室': inquiry_classroom,
    '查询课表': inquiry_schedule,
    '修改密码': modify_password,
    '自主选课': test,
}
