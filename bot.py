from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
from secret import username, password


class GladiatusBot():

    def __init__(self, username, password):
        path = 'C:\Program Files (x86)\chromedriver.exe'
        self.driver = webdriver.Chrome(path)
        self.username = username
        self.password = password

    def login(self):
        self.driver.get(
            'https://lobby.gladiatus.gameforge.com/ro_RO/?kid=a-03733-02233-1812-b350715f&gclid=EAIaIQobChMI86_9mfa16gIViKkYCh0L4A84EAAYASAAEgLpxfD_BwE&mod=start&submod=index')
        time.sleep(3)
        login = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[2]/ul/li[1]/span')
        login.click()
        login = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/div/div[2]/div[2]/div/form/div[1]/div/input')
        login.send_keys('stroeandrei483@gmail.com')
        login = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/div/div[2]/div[2]/div/form/div[2]/div/input')
        login.send_keys('Sad1996.')
        login = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/div/div[2]/div[2]/div/form/p/button[1]/span')
        login.click()
        time.sleep(3)
        login = self.driver.find_element_by_xpath('//*[@id="joinGame"]/a/button/span')
        login.click()
        time.sleep(2)
        login = self.driver.find_element_by_xpath(
            '//*[@id="accountlist"]/div/div[1]/div[2]/div/div/div[11]/button/span')
        login.click()
        time.sleep(3)
        self.driver.get(
            'https://s1-ro.gladiatus.gameforge.com/game/index.php?mod=map&submod=city&sh=dae86c24e7240eea589ehttps://s1-ro.gladiatus.gameforge.com/game/index.php?mod=overview&login=1&sh=a3946fe9cdb658318b407f4f2cfd38a8ca02bcd88154-gdhdfhdfhdfhdfhd')

    def switchTab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def trainer(self):
        trainer = self.driver.find_element_by_xpath('//*[@id="submenu1"]/a[2]')
        trainer.click()
        time.sleep(3)

    def gainPower(self):
        money = int(self.driver.find_element_by_xpath('//*[@id="sstat_gold_val"]').text)
        while money !=0:
            # Strength
            trainer = int(self.driver.find_element_by_xpath('//*[@id="training_box"]/div[2]/div[2]/div').text)
            if money > trainer:
                money = money - trainer;
                print("You have", money, " golds")
                cost = self.driver.find_element_by_xpath('//*[@id="training_box"]/div[2]/div[2]/a')
                cost.click()
            # Dexterity
            trainer = int(self.driver.find_element_by_xpath('//*[@id="training_box"]/div[3]/div[2]/div').text)
            if money > trainer:
                money = money - trainer;
                print("You have", money, " golds")
                cost = self.driver.find_element_by_xpath('//*[@id="training_box"]/div[3]/div[2]/a')
                cost.click()
            # Agility
            trainer = int(self.driver.find_element_by_xpath('//*[@id="training_box"]/div[4]/div[2]/div').text)
            if money > trainer:
                money = money - trainer;
                print("You have", money, " golds")
                cost = self.driver.find_element_by_xpath('//*[@id="training_box"]/div[4]/div[2]/a')
                cost.click()
            # Resistence
            trainer = int(self.driver.find_element_by_xpath('//*[@id="training_box"]/div[5]/div[2]/div').text)
            if money > trainer:
                money = money - trainer;
                print("You have", money, " golds")
                cost = self.driver.find_element_by_xpath('//*[@id="training_box"]/div[5]/div[2]/a')
                cost.click()
            # Charisma
            trainer = int(self.driver.find_element_by_xpath('//*[@id="training_box"]/div[6]/div[2]/div').text)
            if money > trainer:
                money = money - trainer;
                print("You have", money, " golds")
                cost = self.driver.find_element_by_xpath('//*[@id="training_box"]/div[6]/div[2]/a')
                cost.click()
            # Intelect
            trainer = int(self.driver.find_element_by_xpath('//*[@id="training_box"]/div[7]/div[2]/div').text)
            if money > trainer:
                money = money - trainer;
                print("You have", money, " golds")
                cost = self.driver.find_element_by_xpath('//*[@id="training_box"]/div[7]/div[2]/a')
                cost.click()


