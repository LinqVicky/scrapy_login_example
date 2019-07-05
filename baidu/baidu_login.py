# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from time import sleep
import traceback


class BaiDu():
    """
    Selenium登陆百度
    """

    def __init__(self, username, password):
        """
        初始化
        """
        options = webdriver.ChromeOptions()
        # 设置为开发者模式，避免被识别
        options.add_experimental_option('excludeSwitches',
                                        ['enable-automation'])
        self.browser = webdriver.Chrome(options=options)
        self.url = 'https://passport.baidu.com/v2/?login&tpl=mn&u=http%3A%2F%2Fwww.baidu.com%2F&sms=5'
        self.browser.get(self.url)
        self.wait = WebDriverWait(self.browser, 10, 0.2)
        self.username = username
        self.password = password


    def isElementExists(self, name):
    	try:
    		self.wait.until(EC.presence_of_element_located((By.ID, name)))
    		return True
    	except TimeoutException as e:
    		return False
    	except NoSuchElementException as e:
    		return False


    def login(self):
    	try:
    		# 执行JS脚本修改标签css属性，显示出用户名登录div,隐藏扫码div

    		# display: none; visibility: hidden; opacity: 1; 	#扫码div ID="TANGRAM__PSP_3__qrcode"
    		# display: block; visibility: visible; opacity: 1; 	#用户名登录div ID="login"

    		js_code_for_qrcode = 'document.getElementById("TANGRAM__PSP_3__qrcode").setAttribute("style", "display: none; visibility: hidden; opacity: 1;");'
    		js_code_for_login = 'document.getElementById("login").setAttribute("style", "display: block; visibility: visible; opacity: 1;");'

    		self.browser.execute_script(js_code_for_qrcode)
    		self.browser.execute_script(js_code_for_login)

    		sleep(1)

    		username = self.wait.until(EC.element_to_be_clickable((By.ID, 'TANGRAM__PSP_3__userName')))
    		username.clear()
    		username.send_keys(self.username)
    		sleep(1)

    		passwd = self.wait.until(EC.element_to_be_clickable((By.ID, 'TANGRAM__PSP_3__password')))
    		passwd.clear()
    		passwd.send_keys(self.password)
    		sleep(2)
    		
    		btn_login = self.wait.until(EC.element_to_be_clickable((By.ID, 'TANGRAM__PSP_3__submit')))
    		sleep(3.5)
    		btn_login.click()

    		sleep(5)

    		if self.isElementExists('s_username_top'):
    			print('='* 30)
    			print('load successfully')
    			print(self.browser.get_cookies())
    		else:
    			print('load failed')

    	except Exception as e:
    		# raise e
    		print('=' * 30)
    		traceback.print_exc()
    		print('=' * 30)
    	finally:
    		self.browser.close()

		
if __name__ == '__main__':

	ACCOUNT = input('请输入您的账号:')
	PASSOWRD = input('请输入您的密码:')

	test = BaiDu(ACCOUNT, PASSOWRD)  # 输入账号和密码
	test.login()



