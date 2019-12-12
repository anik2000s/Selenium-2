from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome('C:\\Users\\HP\\Downloads\\chromedriver_win32\\chromedriver')
browser.get('https://www.codechef.com/')
username = browser.find_element_by_name('name')
password = browser.find_element_by_name('pass')
username.send_keys('') # username
password.send_keys('') # password
login = browser.find_element_by_name('op')
login.submit()