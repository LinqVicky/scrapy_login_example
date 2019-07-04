# -*- coding: utf-8 -*-
import requests
from urllib.parse import urlencode
import time
import re
# import tesserocr
from PIL import Image
# from aip import AipOcr

"""
info: 果壳网模拟登录，图形验证码
author:
update_time:2019-7-3
"""

"""
csrf_token: 1562143236.63##0b20712022047d3584a1cd1d5e718ff7849644ae	# 页面获取
username: 18350282520
password: Ldq5635132.+-
captcha: lvc8	# OCR识别
captcha_rand: 2316271577 # 页面获取
permanent: y # 是否记住
"""

APP_ID = 'XXX'
API_KEY = 'XXX'
SECRET_KEY = 'XXX'
# client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


headers = {
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Host': 'account.guokr.com',
    'Pragma': 'no-cache',
    # 'Cookie': '__utmt=1; __utma=253067679.2102330349.1540780238.1540780238.1541122809.2; __utmb=253067679.12.9.1541122812936; __utmc=253067679; __utmz=253067679.1540780238.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=253067679.|1=Is%20Registered=No=1; session=afcf1b0f-c71b-43d2-8046-f60ae28f9b45',
    'Referer': 'https://account.guokr.com/sign_in/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.61 Safari/537.36'
}

session = requests.Session()

url = 'https://account.guokr.com/sign_in/'
resp = session.get(url, headers=headers)
html = resp.text

csrf_token = re.search(r'id="csrf_token[\s\S]*?(\d+[\s\S]*?)"', html).group(1)
captcha_rand = re.search(r'id="captchaRand[\s\S]*?(\d+)', html).group(1)
img_url = 'https://account.guokr.com/captcha/' + captcha_rand
with open('captcha.jpg', 'wb') as fw:
    fw.write(session.get(img_url, headers=headers).content)

# # 百度文字识别，basicGeneral 通用文字识别未识别出
# image = get_file_content('captcha.jpg')

# """ 调用通用文字识别, 图片参数为本地图片 """
# baidu_captcha_tresult = client.basicGeneral(image);
# print('='* 30)
# print(baidu_captcha_tresult)
# print('='* 30)

# tesserocr 
# TODO图形验证码识别准确率低， 提升待研究
# image = Image.open('captcha.jpg')
# image = image.convert('L') # 图像灰度处理
# threshold = 127 # 二值化阈值，默认为127
# table = []
# for i in range(256):
# 	if i < threshold:
# 		table.append(0)
# 	else:
# 		table.append(1)
# image = image.point(table, '1')
# captcha = tesserocr.image_to_text(image)
# print('='* 30)
# print(captcha)
# print('='* 30)
# 还有一种百度云文字识别
img=Image.open('captcha.jpg')
img.show()

username = '18350282520' # input('请输入用户名：')
password = 'Ldq5635132.+-' # input('请输入密码：')
captcha = input('请输入验证码：')
data = {
    'csrf_token': csrf_token,
    'username': username,
    'password': password,
    'captcha': captcha,#  
    'captcha_rand': captcha_rand , 
    'permanent': 'y ',
}

response = session.post(url, data=data)
with open('response.html', 'w', encoding='utf-8') as fw:
    fw.write(response.text)

time.sleep(5)

print('='* 60)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.61 Safari/537.36'
}

homepage = 'https://www.guokr.com/i/0496062679/'
with open('homepage.html', 'w', encoding='utf-8') as fw:
    res = session.get(homepage, headers=headers)
    fw.write(res.text)
