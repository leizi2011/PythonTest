package com.ui;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebDriver.Navigation;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;


public class Test {
	public static void main(String[] args) throws Exception {
		String URL ="http://www.baidu.com";
		// ���ô�������������ͣ���ȡ��վ��title
		System.setProperty("webdriver.chrome.driver",
				"C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe");
		//System.setProperty("webdriver.firefox.driver",
			//	"D:/Program Files (x86)/Mozilla Firefox/firefox.exe");
		//WebDriver driver = new FirefoxDriver();
		WebDriver driver = new ChromeDriver();
		Navigation navigation = driver.navigate();
		navigation.to(URL);
		WebElement baiduLogin = driver.findElement(By.linkText("��¼"));	
		baiduLogin.click();
		//WebElement baiduLogin1 = driver.findElement(By.name("tj_trtieba"));
		//baiduLogin1.click();
				
		Thread.sleep(10000);
		WebElement rememberuser = driver.findElement(By.id("TANGRAM__PSP_8__userName"));
		rememberuser.sendKeys("�޹�waha�޹�");
		WebElement rememberpa = driver.findElement(By.id("TANGRAM__PSP_8__password"));
		rememberpa.sendKeys("peng2011");
		//��ѡ���Ƿ�ѡ���ж�
		WebElement rememberme = driver.findElement(By.id("TANGRAM__PSP_8__memberPass"));
		if(rememberme.isSelected())
		{
			System.out.println(rememberme.isSelected()+"��ѡ��ѡ��");
		}
		else
		{
			System.out.println(rememberme.isSelected()+"��ѡ��δ��ѡ��");
			rememberme.click();
		}
		
		WebElement rememberlogin = driver.findElement(By.id("TANGRAM__PSP_8__submit"));
		rememberlogin.click();
		System.out.print("ssddsd" + driver.getTitle()+"��¼�ɹ�");
		Thread.sleep(20000);
		WebElement search = driver.findElement(By.id("kw"));
		search.clear();
		search.sendKeys("���");
		WebElement su = driver.findElement(By.id("su"));
		su.click();
		
		//WebElement search1 = driver.findElement(By.cssSelector("#s_ipt"));
		//search1.sendKeys("���");
	}
	
	
	
}

