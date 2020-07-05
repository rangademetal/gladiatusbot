from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

class GladiatusBot():
    def __init__(self):
        path = 'C:\Program Files (x86)\chromedriver.exe'
        self.driver = webdriver.Chrome(path)
    def login(self):
        self.driver.get('https://lobby.gladiatus.gameforge.com/ro_RO/?kid=a-03733-02233-1812-b350715f&gclid=EAIaIQobChMI86_9mfa16gIViKkYCh0L4A84EAAYASAAEgLpxfD_BwE&mod=start&submod=index')
        time.sleep(3)
        login = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[2]/ul/li[1]/span')
        login.click()
        login = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[2]/div/form/div[1]/div/input')
        login.send_keys('stroeandrei483@gmail.com')
        login = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[2]/div/form/div[2]/div/input')
        login.send_keys('Sad1996.')
        login = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[2]/div/form/p/button[1]/span')
        login.click()
        time.sleep(3)
        login = self.driver.find_element_by_xpath('//*[@id="joinGame"]/a/button/span')
        login.click()
        time.sleep(2)
        login = self.driver.find_element_by_xpath('//*[@id="accountlist"]/div/div[1]/div[2]/div/div/div[11]/button/span')
        login.click()