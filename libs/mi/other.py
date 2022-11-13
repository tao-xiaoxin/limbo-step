'''
第三方小米刷步接口
'''
import requests
from utils.fake_useragent import get_browser_user_agents

user_agents = get_browser_user_agents()

header1 = {
    'User-Agent': user_agents
}
header2 = {
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'User-Agent': user_agents
}


def check_code(response):
    try:
        code = response['code']
        if "200" in str(code):
            return True
        else:
            return False
    except:
        return False


def reserve_step1(user, pwd, step):
    url = 'https://api.iculture.cc/api/run/'

    params = {
        "do": "shuabu",
        "user": user,
        'pass': pwd,
        "count": step,
    }
    try:
        response = requests.get(headers=header1, url=url, params=params).json()
        return check_code(response)
    except:
        return False


def reserve_step2(user, pwd, step):
    '''
    :param user: 小米账号
    :param pwd: 小米密码
    :param gte: 最小值
    :param lte: 最大值
    :return:
    '''
    url = 'http://api.kit9.cn/api/xiaomi_sports/api.php'
    data = {'mobile': user, "password": pwd, "step": step}
    try:
        response = requests.post(url=url, headers=header2, data=data).json()
        return check_code(response)
    except:
        return False


def email_step(user, pwd, step):
    url = 'http://api.kit9.cn/api/xiaomi_sports/api_email_fixed.php'
    data = {'email': user, "password": pwd, "step": step}
    try:
        response = requests.post(url=url, headers=header2, data=data).json()
        return check_code(response)
    except:
        return False
