from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get('https://www.processon.com/login?f=index')
    browser.find_element_by_xpath('//*[@id="login_email"]').send_keys('1060600880@qq.com')
    browser.find_element_by_xpath('//*[@id="login_password"]').send_keys('xxxxx')
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="signin_btn"]').click()
    time.sleep(3)
    # cookies = browser.get_cookies() # 获取cookies
    # print(cookies)
    # time.sleep(3)
except Exception as e:
    print(e)
finally:    
    browser.close()