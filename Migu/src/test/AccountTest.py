import unittest
from selenium import webdriver
from time import sleep
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
        driver.find_element_by_xpath("//*[@id='nav']/li[5]").click()
        sleep(5)
        driver.find_element_by_xpath("//*[@id='subnav']/li/a").click()
        driver.refresh()  
        driver.find_element_by_xpath("//*[@id='J_users']/div/div[1]/a[2]").click()
        sleep(4)
        driver.find_element_by_xpath("//*[@id='field-userName']").send_keys("penglei")
        driver.find_element_by_name("realName").send_keys("penglei")
        driver.find_element_by_name("userEmail").send_keys("709320@qq.com")
        driver.find_element_by_id("field-userMobile").send_keys("18765612345")
        driver.find_element_by_id("fields-roleIds").click()
        driver.find_element_by_xpath("//*[@id='fields-roleIds']/option[3]").click()
        driver.find_element_by_id("field-userPassword1").send_keys("123456")
        driver.find_element_by_id("field-userPassword2").send_keys("123456")
        driver.find_element_by_css_selector("#J_addUser > div.actions > a.button.cancel.cancel-button").click()
        sleep(3)
        ele=driver.find_element_by_class_name("dialog-buttons")
        ele.find_element_by_tag_name("button").click()
        #driver.find_element_by_css_selector("#J_addUser > div.actions > a.button.save.save-button").click()
        
     def tearDown(self):
         pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()