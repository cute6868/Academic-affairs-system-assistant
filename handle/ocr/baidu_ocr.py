# BaiDu-OCR 文档: https://cloud.baidu.com/doc/OCR/s/wkibizyjk

from aip import AipOcr
from utils import get_json_data


class ocr:

    def __init__(self, image_binary):
        # 从json文件中读取数据
        info = get_json_data('./res/system.json').get('BaiDu_OCR')

        # API接口-配置信息
        self._APP_ID = info.get('APP_ID')
        self._API_KEY = info.get('API_KEY')
        self._SECRET_KEY = info.get('SECRET_KEY')

        # 创建客户端对象
        client = AipOcr(self._APP_ID, self._API_KEY, self._SECRET_KEY)

        # 如果有可选参数
        options = {}
        options["language_type"] = "ENG"
        options["detect_direction"] = "true"
        options["probability"] = "true"

        try:
            # 调用通用文字识别（高精度版）
            self.text = client.basicAccurate(image_binary, options).get('words_result')[0].get('words')
        except Exception as e:
            self.text = 'Error4'
            with open('./log.txt', 'a', encoding='utf-8') as f:
                f.write(f'[Error]: {e}\n')
