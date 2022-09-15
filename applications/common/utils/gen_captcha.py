from captcha.image import ImageCaptcha, random_color

from PIL import Image
from random import choices


def gen_captcha(content='2345689abcdefghijklmnpqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ'):
    """ 生成验证码 """
    image = ImageCaptcha()

    # 获取字符串
    captcha_text = "".join(choices(content, k=4)).lower()
    print("captcha_text", captcha_text)
    # 生成图像
    captcha_image = Image.open(image.generate(captcha_text))
    print("captcha_image", captcha_image)
    '''
    '''
    # 样式设置
    rgb = (38, 38, 0)  # 字体色
    bgc = (255, 255, 255)  # 背景色
    color = random_color(50, 180)  # 生成随机颜色
    print(color)
    result = image.create_captcha_image(captcha_text, rgb, bgc)
    tt = image.create_noise_dots(image=result, color=color, width=10, number=10)
    image.create_noise_curve(image=result, color=rgb)

    return captcha_text, captcha_image
