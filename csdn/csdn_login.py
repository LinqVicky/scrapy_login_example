import time
import traceback
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
# import re


def login():

    acount_num =  input('请输入账号:\n')
    passwd_str =  input('请输入密码:\n')

    options = webdriver.ChromeOptions()
    # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # 不显示窗体 
    # options.add_argument('--headless')
    # 不加载图片,加快访问速度
    # options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
    browser = webdriver.Chrome(options=options)
    browser.set_window_size(1920, 1080)
    wait = WebDriverWait(browser, 20)

    try:
        url = 'https://passport.csdn.net/login?code=public'
        browser.get(url)

        # 找到账号登陆并点击
        input_button = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="main-select"]/ul/li[2]/a')))
        input_button.click()

        # 输入账号
        input_element = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="col-xs-12 col-sm-12 control-col-pos col-pr-no col-pl-no"]/input')))
        input_element.send_keys(acount_num)

        # 输入密码
        input_password = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="col-xs-12 col-sm-12 control-col-pos col-pr-no col-pl-no"]/input[@id="password-number"]')))
        input_password.send_keys(passwd_str)

        # 点击登陆
        touch_button = wait.until(EC.presence_of_element_located((By.XPATH, '//button')))
        touch_button.click()
        time.sleep(5)
        cur_cookies = browser.get_cookies()[0]
        print('=' * 50)
        print(cur_cookies)
        print('=' * 50)


    except Exception as e:
        print('=' * 30)
        traceback.print_exc()
        print('=' * 30)
    finally:
        browser.close()


if __name__ == '__main__':
    login()
