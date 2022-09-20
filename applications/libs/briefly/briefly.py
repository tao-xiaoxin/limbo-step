'''
每日一言
'''
import requests


def get_briefly():
    remark = requests.get("https://www.zibll.com/wp-content/themes/zibll/yiyan/qv-yiyan.php").text
    return remark
