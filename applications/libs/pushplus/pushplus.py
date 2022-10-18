"""
推送加sdk
推送加接口文档地址:http://www.pushplus.plus/doc/guide/api.html
"""
import requests


def send_push(
    token,
    title,
    content,
    template="markdown",
    channel="wechat",
    webhook="",
    callbackUrl="",
    timestamp='',
):
    """
    :param
        token : 用户令牌，可直接加到请求地址后，如：http://www.pushplus.plus/send/{token}?content=XXX
        title : 消息标题
        content : 消息内容
        template : 发送消息模板,可选:html,json,txt,markdown,cloudMonitor
        channel :
            wechat:微信公众号,默认发送渠道
            webhook:第三方webhook服务；企业微信机器人、钉钉机器人、飞书机器人
            cp:企业微信应用
            mail:邮件
            sms:短信；收费使用，1条短信扣减10积分
        webhook : webhook编码
        callbackUrl : 回调地址，异步回调发送结果
    """
    params = {
        "token": token,
        "title": title,
        "content": content,
        "template": template,
        "channel": channel,
        "webhook": webhook,
        "callbackUrl": callbackUrl,
        "timestamp": timestamp,
    }
    url = "http://www.pushplus.plus/send"
    result = requests.get(url, params=params).json()
    return result
