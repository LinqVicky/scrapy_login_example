from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException,NoSuchElementException
import traceback
from time import sleep
import tesserocr
from PIL import Image
import base64



class ZhiHu():
    """
    登陆知乎
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
        self.url = 'https://www.zhihu.com/signin'
        self.browser.get(self.url)
        self.wait = WebDriverWait(self.browser, 10, 0.2)
        self.username = username
        self.password = password

    def isElementExists(self, name):
    	try:
    		self.browser.find_element_by_name(name)
    		return True
    	except NoSuchElementException as e:
    		return False

    def login(self):
        """
        打开浏览器,并且输入账号密码
        :return: None
        """
        try:
            # self.browser.get(self.url)
            username = self.wait.until(EC.element_to_be_clickable((By.NAME, 'username')))
            password = self.wait.until(EC.element_to_be_clickable((By.NAME, 'password')))
            sleep(1)
            username.send_keys(self.username)
            sleep(1)
            password.send_keys(self.password)
            sleep(1)

            # 是否出现验证码
            if self.isElementExists('captcha'):
                # 获取验证码图片数据
                captcha = self.wait.until(EC.presence_of_element_located((By.NAME, 'captcha')))
                captcha_img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'Captcha-englishImg'))).get_attribute('src')
                print(captcha_img)
                im_base64 = captcha_img.split(',')[1]  #拿到base64编码的图片信息
                im_bytes = base64.b64decode(im_base64)  #转为bytes类型
                with open('captcha_img.jpg','wb') as f:  #保存图片到本地
                    f.write(im_bytes)
                # tesserocr 
                # TODO图形验证码识别准确率低， 提升待研究
                image = Image.open('captcha_img.jpg')
                image = image.convert('L') # 图像灰度处理
                threshold = 127 # 二值化阈值，默认为127
                table = []
                for i in range(256):
                    if i < threshold:
                        table.append(0)
                    else:
                        talbe.append(1)
                image = image.point(table, '1')
                image.save('zhihu\captcha\captcha_1.png')
                # captcha_result = tesserocr.image_to_text(image)
                # print(captcha_result)
                img=Image.open('captcha.jpg')
                img.show()
                captcha_result = input('请输入验证码')
                captcha.send_keys(captcha_result)
                sleep(1)

            # <a class="btn btn-login">登录</a>
            btn_login = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'SignFlow-submitButton')))
            sleep(0.5)
            
            btn_login.click()
            sleep(3)
            success = self.wait.until(EC.element_to_be_clickable((By.ID, 'Popover24-toggle')))
            print(self.browser.get_cookies())
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

    test = ZhiHu(ACCOUNT, PASSOWRD)  # 输入账号和密码
    test.login()
