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

    acount_num = 'victor_linq@126.com'	# input('请输入账号:\n')
    passwd_str = 'Ldq102744'	# input('请输入密码:\n')
  
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

        url = 'http://mail.126.com/'
        browser.get(url)
        '''
        # 由于是iframe，通过点击密码登录切换到的页面无法获取到该子iframe里面的节点
        account_login = wait.until(EC.presence_of_element_located((By.ID, 'switchAccountLogin')))
        time.sleep(1)
        account_login.click()
        '''
        account_login = wait.until(EC.presence_of_element_located((By.ID, 'switchAccountLogin')))
        time.sleep(1)
        account_login.click()
        # 126登陆框是使用iframe进行嵌套的，所以需要先切换到该iframe

        # elem = wait.until(EC.presence_of_element_located((By.ID, "iframe[id^='x-URS-iframe']")))
        elem = browser.find_element_by_css_selector("iframe[id^='x-URS-iframe']") #  no such element
        print('=' * 30) 
        print(elem.get_attribute('id'))
        print(elem.get_attribute('src'))
        print('=' * 30)
        # https://passport.126.com/webzj/v1.0.1/pub/index_dl2_new.html?cd=https%3A%2F%2Fmimg.127.net%2Fp%2Ffreemail%2Findex%2Funified%2Fstatic%2F2019%2Fcss%2F&cf=urs.126.589bdb88.css&MGID=1561986487983.4104&wdaId=&pkid=QdQXWEQ&product=mail126
        browser.switch_to.frame(elem)
        time.sleep(1)


      
        # acount = browser.find_element_by_name('email')
        acount = wait.until(EC.presence_of_element_located((By.NAME, 'email')))
        passwd = wait.until(EC.presence_of_element_located((By.NAME, 'password')))
        print('=' * 30) 
        print(acount.get_attribute('name')) 
        print(passwd.get_attribute('name')) 
        print('=' * 30)
        # email  节点选择没错
        # selenium.common.exceptions.InvalidElementStateException: 
        # Message: invalid element state: Element is not currently interactable and may not be manipulated
        acount.clear()
        acount.send_keys(acount_num)

        # passwd = browser.find_element_by_name('password')
        # passwd = wait.until(EC.visibility_of_element_located((By.NAME, 'password')))
        passwd.clear()
        passwd.send_keys(passwd_str)

        time.sleep(3)
        # click_button = browser.find_element_by_id('dologin')
        click_button = wait.until(EC.presence_of_element_located((By.ID,'dologin')))
        click_button.click()
        time.sleep(5)
        cur_cookies = browser.get_cookies()[0]
        print('=' * 50)
        print(cur_cookies)
        print('=' * 50)

    except Exception as e:
        
        print('=' * 30)
        traceback.print_exc()
        print('=' * 30)
        # raise e
    finally:
        browser.close()    


if __name__ == '__main__':
    login()
