from selenium import webdriver
import time
# 用户名与密码单独写在同级目录下的private.py文件，并添加到.gitignore
from private import processon_name, processon_password


try:
    browser = webdriver.Chrome()

    browser.get("https://processon.com/")
    time.sleep(3)

    # 获取登陆按钮并单击
    login_button = browser.find_element_by_xpath("/html/body/header/ul/li[5]/a")
    login_button.click()
    time.sleep(3)

    # 输入用户名与密码
    browser.find_element_by_xpath('//*[@id="login_email"]').send_keys(processon_name)
    browser.find_element_by_xpath('//*[@id="login_password"]').send_keys(processon_password)
    time.sleep(3)

    # 单击登陆
    browser.find_element_by_xpath('//*[@id="signin_btn"]').click()
    time.sleep(5)

except Exception as es:
    print(es)

finally:
    browser.close()






