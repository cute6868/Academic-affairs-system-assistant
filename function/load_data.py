import json
from .base import show_message


def load_data(*args):
    with open('./res/data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        args[0].delete(1.0, 'end')
        args[0].insert('insert', json.dumps(data, indent=4, ensure_ascii=False))
    show_message('提示', '    刷新成功！    ')
