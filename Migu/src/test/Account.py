import unittest,sys
from selenium import webdriver
from time import sleep
class Account():
    def setUp(self):
        self.driver=webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
    def testName(self):
        driver =self.driver    
        driver.implicitly_wait(1)
        driver.get("http://192.168.16.4:8080/MIGU-RPT/webside/index.action")
        driver.find_element_by_xpath("/html/body/div[1]/form/p[1]/input").send_keys("admin")
        driver.find_element_by_xpath("/html/body/div[1]/form/p[2]/input").send_keys("111111")
        driver.find_element_by_xpath("/html/body/div[1]/form/p[5]/button").click();
        sleep(5)     
        driver.find_element_by_xpath("//*[@id='nav']/li[5]").click()
        driver.find_element_by_xpath("//*[@id='breadcrumb']/span").click()
        driver.refresh()  
        driver.find_element_by_xpath("//*[@id='J_users']/div/div[1]/a[2]")
    def tearDown(self):
        pass
    if __name__ == '__main__':
      reload(sys)
      #sys.setdefaultencoding('utf-8')
      