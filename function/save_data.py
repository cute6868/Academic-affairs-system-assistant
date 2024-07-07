import json
from .base import show_message


def save_data(*args):
    content = args[0].get(1.0, 'end')
    try:
        data = json.loads(content)
        with open('./res/data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        show_message('提示', '    保存成功！    ')
    except json.JSONDecodeError:
        print("Invalid JSON format")
