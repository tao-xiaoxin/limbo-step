# -*- coding: utf8 -*-
'''
PUSHPLUS推送 官网为https://www.pushplus.plus/
'''
import requests, json
from configs.config import configs


# PUSHPLUS推送
def plus_send(msg, title='凌波微步运动助手', template='markdown'):
    if configs.PLUS_TOKEN == '':
        return False
    url = 'http://www.pushplus.plus/send'
    data = {
        "token": configs.PLUS_TOKEN,
        "title": title,
        "content": msg,
        "template": template
    }
    body = json.dumps(data).encode(encoding='utf-8')
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=body, headers=headers)
    if response.status_code == 200:
        return True
    return False
