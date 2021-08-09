# -*- coding: utf8 -*-
import requests, time, re,sys, json, random

# 设置开始
# 用户名（格式为 13800138000）
user1 = sys.argv[1]
# 登录密码
passwd1 = sys.argv[2]

# 酷推skey和server酱sckey和企业微信设置，只用填一个其它留空即可
skey = sys.argv[3]
# 推送server酱
sckey = sys.argv[4]
# 企业微信推送
# 是否开启企业微信推送false关闭true开启，默认关闭，开启后请填写设置并将上面两个都留空
position = sys.argv[5]
base_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?'
req_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='
corpid = sys.argv[6]  # 企业ID， 登陆企业微信，在我的企业-->企业信息里查看
corpsecret = sys.argv[7]  # 自建应用，每个自建应用里都有单独的secret
agentid = sys.argv[8]  # 填写你的应用ID，不加引号，是个整型常数,就是AgentId
touser = sys.argv[9]  # 指定接收消息的成员，成员ID列表（多个接收者用‘|’分隔，最多支持1000个）。特殊情况：指定为”@all”，则向该企业应用的全部成员发送
toparty = sys.argv[10]  # 指定接收消息的部门，部门ID列表，多个接收者用‘|’分隔，最多支持100个。当touser为”@all”时忽略本参数
totag = sys.argv[11]  # 指定接收消息的标签，标签ID列表，多个接收者用‘|’分隔，最多支持100个。当touser为”@all”时忽略本参数

# （用于测试推送如果改了能收到推送，推送设置就没问题，看看是不是set_push列表里面没设置推送，仔细看下面我写的很详细）要修改的步数，直接输入想要修改的步数值，（默认）留空为随机步数，改了这个直接运行固定值（用于测试推送）
# 测试好记得留空不然一直提交固定步数
step1 = ""

# 开启根据地区天气情况降低步数（默认关闭）
open_get_weather = sys.argv[12]
# 设置获取天气的地区（上面开启后必填）如：area = "宁波"
area = sys.argv[13]

# 以下如果看不懂直接默认就行只需改上面

# 系数K查询到天气后降低步数比率，如查询得到设置地区为多云天气就会在随机后的步数乘0.9作为最终修改提交的步数
K_dict = {"多云": 0.9, "阴": 0.8, "小雨": 0.7, "中雨": 0.5, "大雨": 0.4, "暴雨": 0.3, "大暴雨": 0.2, "特大暴雨": 0.2}

# 设置运行程序时间点,24小时制（不要设置0，1，2可能会发生逻辑错误），这边设置好云函数触发里也要改成相同的小时运行，与time_list列表对应，如默认：30 0 8,10,13,15,17,19,21 * * * *，不会的改8,10,13,15,17,19,21就行替换成你要运行的时间点，其它复制
# 默认表示为8点10点13点15点17点19点21点运行,如需修改改time_list列表，如改成：time_list = [7, 9, 13, 15, 17, 19, 20]就表示为7点9点13点15点17点19点20点运行，云函数触发里面也要同步修改
# 说白了不是刷七次嘛,你希望在什么时候刷,设七个时间点，不要该成0，1，2（就是不要设置0点1点2点运行），其它随便改。如果要刷的次数小于7次多余的时间点不用改保持默认就行如只需要4次就改前4个，但函数触发里面要改成4个的，不能用7个的
time_list = [8, 10, 13, 15, 17, 19, 21]

# 设置运行结果推送不推送与上面时间一一对应，如：set_push列表内的第一个值与time_list列表内的第一个时间点对应，该值单独控制该时间点的推送与否（默认表示为21点（就是设置的最后一个时间点）推送其余时间运行不推送结果）
# 也是改列表内的False不推送，True推送，每个对应上面列表的一个时间点，如果要刷的次数小于7次同样改前几个其它默认
set_push = [True, True, True, True, True, True, True]

# 最小步数（如果只需要刷步的次数少于7次就将该次数以后的步数全都改成0，如：time_list[3]: 0，表示第五次开始不运行或者直接云函数触发里面不在该时间调用均可（建议用后者））
min_dict = {time_list[0]: 400, time_list[1]: 10000, time_list[2]: 20000, time_list[3]: 30000, time_list[4]: 40000, time_list[5]: 50000, time_list[6]: 60000}
# 最大步数（例如现在设置意思是在8点（你设置的第一个时间点默认8）运行会在1500到2999中随机生成一个数提交（开启气候降低步数会乘系数K）10点3000~4999。。。以此类推，步数范围建议看懂了再改，没看懂直接默认就好）
max_dict = {time_list[0]: 9999, time_list[1]: 19999, time_list[2]: 29999, time_list[3]: 39999, time_list[4]: 49999, time_list[5]: 59999, time_list[6]: 69999}
# 设置结束
now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
headers = {'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; MI 6 MIUI/20.6.18)'}


#获取区域天气情况
def getWeather():
    global K, type
    url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + area
    hea = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(url=url, headers=hea)
    print(r)
    if r.status_code == 200:
        result = r.text
        res = json.loads(result)
        print(res)
        if "多云" in res['data']['forecast'][0]['type']:
            K = K_dict["多云"]
        elif "阴" in res['data']['forecast'][0]['type']:
            K = K_dict["阴"]
        elif "小雨" in res['data']['forecast'][0]['type']:
            K = K_dict["小雨"]
        elif "中雨" in res['data']['forecast'][0]['type']:
            K = K_dict["中雨"]
        elif "大雨" in res['data']['forecast'][0]['type']:
            K = K_dict["大雨"]
        elif "暴雨" in res['data']['forecast'][0]['type']:
            K = K_dict["暴雨"]
        elif "大暴雨" in res['data']['forecast'][0]['type']:
            K = K_dict["大暴雨"]
        elif "特大暴雨" in res['data']['forecast'][0]['type']:
            K = K_dict["特大暴雨"]
        type = res['data']['forecast'][0]['type']
        print(K)
        print(type)
    else:
        print("获取天气情况出错")


#获取北京时间确定随机步数&启动主函数
def getBeijinTime():
    global K, type
    K = 1.0
    type = ""
    hea = {'User-Agent': 'Mozilla/5.0'}
    url = r'http://time1909.beijing-time.org/time.asp'
    if open_get_weather:
        getWeather()
    r = requests.get(url=url, headers=hea)
    if r.status_code == 200:
        result = r.text
        #print(result)
        if "nhrs=" + str(time_list[0]) in result:
            a = set_push[0]
            min_1 = min_dict[time_list[0]]
            max_1 = max_dict[time_list[0]]
        elif "nhrs=" + str(time_list[1]) in result:
            a = set_push[1]
            min_1 = min_dict[time_list[1]]
            max_1 = max_dict[time_list[1]]
        elif "nhrs=" + str(time_list[2]) in result:
            a = set_push[2]
            min_1 = min_dict[time_list[2]]
            max_1 = max_dict[time_list[2]]
        elif "nhrs=" + str(time_list[3]) in result:
            a = set_push[3]
            min_1 = min_dict[time_list[3]]
            max_1 = max_dict[time_list[3]]
        elif "nhrs=" + str(time_list[4]) in result:
            a = set_push[4]
            min_1 = min_dict[time_list[4]]
            max_1 = max_dict[time_list[4]]
        elif "nhrs=" + str(time_list[5]) in result:
            a = set_push[5]
            min_1 = min_dict[time_list[5]]
            max_1 = max_dict[time_list[5]]
        elif "nhrs=" + str(time_list[6]) in result:
            a = set_push[6]
            min_1 = min_dict[time_list[6]]
            max_1 = max_dict[time_list[6]]
        else:
            a = False
            min_1 = 0
            max_1 = 0
            if step1 != "":
                min_1 = 1
                max_1 = 1
        if step1 != "":
            a = True
        min_1 = int(K * min_1)
        max_1 = int(K * max_1)
    else:
        print("获取北京时间失败")
        return
    if min_1 != 0 and max_1 != 0:
        main(min_1, max_1, a)
    else:
        print("当前不是主人设定的提交步数时间或者主人设置了0步数呢，本次不提交")
        return

def change_step(user, password, step):
    url = 'https://run.nanjin1937.com/API/s_xm.php'
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 QQ/8.8.17.612 V1_IPH_SQ_8.8.17_1_APP_A Pixel/1125 MiniAppEnable SimpleUISwitch/0 StudyMode/0 QQTheme/1102 Core/WKWebView Device/Apple(iPhone X) NetType/4G QBWebViewType/1 WKType/1'

    }
    data = {
        'phone':user,
        'password':password,
        'step':step
    }
    print(data)
    response = requests.post(url=url,headers=headers,data=data).text
    return response

# 主函数
def main(min_1, max_1, a):
    user = str(user1)
    password = str(passwd1)
    step = str(step1)
    if user == '' or password == '':
        print("用户名或密码填写有误！")
        return

    if step == '':
        print("已设置为随机步数(" + str(min_1) + "~" + str(max_1) + ")")
        step = str(random.randint(min_1, max_1))
    else:
        step = str(step)
    response=change_step(user, password, step)
    _add = ""
    if K != 1.0:
        _add = "\n" + type + "已设置降低步数,系数为" + str(K)
    result = '['+now+']' +_add+'\n修改步数（'+step+'）' + response
    print(result)
    if a:
        push('【小米运动步数修改】', result)
        push_wx(result)
        run(result)
    else:
        print("此次修改结果不推送")
    return result

# 获取时间戳
def get_time():
    url = 'http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp'
    response = requests.get(url, headers=headers).json()
    t = response['data']['t']
    return t

#发送酷推
def push(title, content):
    if skey == "NO":
        return
    else:
        url = "https://push.xuthus.cc/send/" + skey
        data = title + "\n" + content
        # 发送请求
        res = requests.post(url=url, data=data.encode('utf-8')).text
        # 输出发送结果
        print(res)

# 推送server
def push_wx(desp=""):
    if sckey == 'NO':
        return
    else:
        server_url = "https://sc.ftqq.com/{sckey}.send"
        params = {
            "text": '【小米运动步数修改】',
            "desp": desp
        }

        response = requests.get(server_url, params=params).text
        print(response)

# 企业微信
def get_access_token():
    urls = base_url + 'corpid=' + corpid + '&corpsecret=' + corpsecret
    resp = requests.get(urls).json()
    access_token = resp['access_token']
    return access_token

def run(msg):
    if position:
        data = {
            "touser": touser,
            "toparty": toparty,
            "totag": totag,
            "msgtype": "text",
            "agentid": agentid,
            "text": {
                "content": "【小米运动步数修改】\n" + msg
            },
            "safe": 0,
            "enable_id_trans": 0,
            "enable_duplicate_check": 0,
            "duplicate_check_interval": 1800
        }
        data = json.dumps(data)
        req_urls = req_url + get_access_token()
        resp = requests.post(url=req_urls, data=data).text
        print(resp)
        return resp
    else:
        return

def main_handler(event, context):
    getBeijinTime()

if __name__ == "__main__":
    getBeijinTime()
