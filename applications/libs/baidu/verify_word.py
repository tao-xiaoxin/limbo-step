# encoding:utf-8
'''
用于用户登录注册名称文本内容审核
'''
import requests
from applications.configs.config import BaseConfig

baidu_config = BaseConfig()


def get_access_token():
    '''
    获取百度的 access_token
    '''
    url = 'https://aip.baidubce.com/oauth/2.0/token'
    data = {
        'grant_type': 'client_credentials',
        'client_id': baidu_config.BAIDU_API_KEY,  # 百度云应用的AK
        'client_secret': baidu_config.BAIDU_SECRET_KEY,  # 百度云应用的SK
    }
    access_token = requests.get(url=url, params=data).json()['access_token']
    return access_token


def get_conclusion(text):
    '''
    获取文本审核内容结论
    '''
    url = "https://aip.baidubce.com/rest/2.0/solution/v1/text_censor/v2/user_defined"
    params = {"text": text}
    request_url = url + "?access_token=" + get_access_token()
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers).json()
    return response
