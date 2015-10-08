# -*- coding: utf-8 -*-  
import unittest,sys
from selenium import webdriver
from time import sleep
import HTMLTestRunner
import os

class Test(unittest.TestCase):
    def setUp(self):
        #need to set chrome dir
        self.driver=webdriver.Chrome("C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe")
        #self.driver=webdriver.Firefox()
    def testName(self):
        driver =self.driver    
        driver.implicitly_wait(1)
        driver.get("http://192.168.16.4:8080/MIGU-RPT/webside/index.action")
        driver.find_element_by_xpath("/html/body/div[1]/form/p[1]/input").send_keys("admin")
        driver.find_element_by_xpath("/html/body/div[1]/form/p[2]/input").send_keys("111111")
        driver.find_element_by_xpath("/html/body/div[1]/form/p[5]/button").click();
        sleep(5)     
        driver.find_element_by_xpath("/html/body/div[2]/ul[1]/li[1]/a").click()
        driver.find_element_by_xpath("/html/body/div[2]/ul[2]/li[1]/a").click()
        
        #driver.find_element_by_link_text(u"统计分析").click()
        #driver.find_element_by_link_text(u"产品使用Top10").click()
        driver.refresh()  
        #driver.find_element_by_css_selector("li.selected").click()      
        #driver.find_element_by_id("searchCompanyId")
        #driver.find_element_by_css_selector("#searchCompanyId > div.select-pull > dl > dd").click()
        #driver.find_element_by_id("target-select").click()
        #driver.find_element_by_css_selector("#target-select > div.select-pull > dl > dd").click()
        #choose cmread
        driver.find_element_by_css_selector("#searchCompanyId > a.select-arrow").click()
        #print driver.find_element_by_xpath("//div[@id='searchCompanyId']/div[1]").get_attribute("select-current")      
        driver.find_element_by_xpath("//div[@id='searchCompanyId']/div[2]/dl/dd[3]").click()
        #driver.find_element_by_xpath("/html/body/div[2]/div[2]/form/div[1]/div/div[2]/dl/dd[2]").click()
        #choose month
        driver.find_element_by_xpath("//ul[@id='cycle']/li[2]/p").click()
        #driver.find_element_by_id("searchDate").click()       
        #driver.find_element_by_xpath("/html/body/div[2]/div[2]/form/div[2]/ul/li[2]/p").click()
        #choose data
        #driver.find_element_by_xpath("/html/body/div[2]/div[2]/form/div[3]/div/div").click()
        
        driver.find_element_by_xpath("//div[@id='searchDate']").click()        
        driver.find_element_by_xpath("html/body/div[6]").click()  #查找元素可以借助F12功能键，获取元素的xpath路径             
        driver.switch_to_frame(driver.find_element_by_xpath("html/body/div[6]/iframe")) #切换到iframe里面
        element=driver.find_element_by_xpath("//tr/td[@onclick='day_Click(2015,7,26);']")#元素展示需要时间延迟
        sleep(4)
        element.click()        
        #execute javascript driver.find_element_by_xpath("//tr/td[@onclick='day_Click(2015,7,26);']").click()
        #ActionChains(driver).context_click(element).perform()
        #driver.find_element_by_xpath("//tr/td[@onclick='day_Click(2015,7,26);']").click()
        driver.switch_to_default_content();#切出iframe到外面数据
        #driver.find_element_by_xpath()

        #driver.find_element_by_css_selector("td.WdayOn").click()
        #driver.find_element_by_xpath("/html/body/div[2]/div[2]/form/div[3]/div/div").click()
    def tearDown(self):
        self.driver.quit()
        
        #self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    
    reload(sys)
    print os.path
    #sys.setdefaultencoding('utf-8')
    #一个TestCase的实例就是一个测试用例，包括测试前准备环境的搭建(setUp)，执行测试代码(run)，以及测试后环境的还原(tearDown)
    #而多个测试用例集合在一起，就是TestSuite，而且TestSuite也可以嵌套TestSuite
    #TestLoader是用来加载TestCase到TestSuite中的，其中有几个loadTestsFrom__()方法
    #就是从各个地方寻找TestCase，创建它们的实例，然后add到TestSuite中，再返回一个TestSuite实例
    #TextTestRunner是来执行测试用例的，其中的run(test)会执行TestSuite/TestCase中的run(result)方法
    suite1 = unittest.TestLoader().loadTestsFromTestCase(Test)#
    suite = unittest.TestSuite([suite1]) #suite = unittest.TestSuite([suite1, suite2]) 测试多个类
    unittest.TextTestRunner(verbosity=2).run(suite) 
    unittest.TextTestResult 
    #unittest.TextTestRunner(verbosity=2).run(suite) 
    # 这个等价于上述但可设置verbosity=2，省去了运行时加-v
       
    filename="./test.html"  #定义个报告存放路径，支持相对路径。
    fp=file(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Report_title',description='Report_description')  #引用外界的测试报告模板
    runner.run(suite)
    
    #unittest.TextTestRunner().run(suite)   
  
    #unittest.main()