'''
第三方小米刷步接口
'''
import requests,random

header1 = {
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; MI 6 MIUI/20.6.18)'
}

header2 = {
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; MI 6 MIUI/20.6.18)'
}

def pig_step(user,pwd,gte,lte):
    url = 'https://api.iculture.cc/api/run/'
    step = str(random.randint(gte, lte))
    params ={
        "do":"shuabu",
        "user":user,
        'pass':pwd,
        "count":step,
    }
    response =requests.get(headers=header1,url=url,params=params).json()
    return response
    


def phone_step(user, pwd, gte, lte):
    '''
    :param user: 小米账号
    :param pwd: 小米密码
    :param gte: 最小值
    :param lte: 最大值
    :return:
    '''
    step = str(random.randint(gte, lte))
    url = 'http://api.kit9.cn/api/xiaomi_sports/api.php'
    data = {'mobile': user, "password": pwd, "step": step}
    response = requests.post(url=url, headers=header2, data=data).json()
    return response


def email_step(user, pwd, gte, lte):
    step = str(random.randint(gte, lte))
    url = 'http://api.kit9.cn/api/xiaomi_sports/api_email_fixed.php'
    data = {'email': user, "password": pwd, "step": step}
    response = requests.post(url=url, headers=header2, data=data).json()
    return response
