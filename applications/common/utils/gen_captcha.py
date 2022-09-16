from captcha.image import ImageCaptcha, random_color

from PIL import Image
from random import choices


def gen_captcha(content='2345689abcdefghijklmnpqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ'):
    """ 生成验证码 """
    c_image = ImageCaptcha()

    # 获取字符串
    captcha_text = "".join(choices(content, k=4)).lower()
    # 样式设置
    rgb = (100, 101, 56)  # 字体色
    bgc = (255, 255, 255)  # 背景色
    # 生成图像
    image = c_image.create_captcha_image(captcha_text, rgb, bgc)
    captcha_image = c_image.create_noise_curve(image=image, color=rgb)
    return captcha_text, captcha_image
