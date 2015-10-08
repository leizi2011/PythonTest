import unittest,sys
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


class Test(unittest.TestCase):
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
        driver.find_element_by_xpath("//*[@id='nav']/li[4]/a").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@id='subnav']/li[1]/a").click()
        driver.refresh()  
        driver.find_element_by_xpath("//*[@id='migu-products']/table/tbody/tr[1]/td[5]/a[2]").click()
        sleep(1)
        driver.find_element_by_id("field-relationId")
        driver.find_element_by_xpath("//*[@id='field-relationId']/option[3]").click()
        sleep(3)
        driver.find_element_by_css_selector("#item-relation-editform > div:nth-child(5) > table > tbody > tr > td:nth-child(3) > ul > li:nth-child(1)").click()            
        driver.find_element_by_class_name("add-related-item").click()
        #driver.find_element_by_class_name("button update update-button").click()
        driver.find_element_by_xpath("//*[@id='J_productRelation']/div[3]/a[1]").click()
        sleep(5)
        driver.find_element_by_xpath("//*[@id='migu-products']/table/tbody/tr[1]/td[5]/a[2]").click()
        sleep(1)
        driver.find_element_by_id("field-relationId")
        driver.find_element_by_xpath("//*[@id='field-relationId']/option[3]").click()
        sleep(3)
        driver.find_element_by_css_selector("##item-relation-editform > div:nth-child(5) > table > tbody > tr > td:nth-child(1) > ul > li > a").click()            
        driver.find_element_by_class_name("remove-related-item").click()
        #driver.find_element_by_class_name("button update update-button").click()
        driver.find_element_by_xpath("//*[@id='J_productRelation']/div[3]/a[1]").click()
     def tearDown(self):
         pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']

     unittest.main()