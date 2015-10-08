package com.example.tests;

import java.sql.Time;

import junit.framework.Assert;

import com.thoughtworks.selenium.*;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;


public class A {

	private Selenium selenium;

	@Before
	public void setUp() throws Exception {
		// System.setProperty("webdriver.firefox.driver",
		// "D:/Program Files (x86)/Mozilla Firefox/firefox.exe");
		selenium = new DefaultSelenium("localhost", 4444,
				"*firefox D:/Program Files (x86)/Mozilla Firefox/firefox.exe",
				"https://www.baidu.com/");
		
		selenium.start();
	}

	@Test
	public void testTest() throws Exception {
		
		
		
		//String keyWordsLocator = "document.getElementById('kw')";     
	   // String search = "document.getElementById('su')";
		// 百度网址
		//selenium.open("/");
		
		selenium.open("https://www.baidu.com/");
		//selenium.click("id=kw");
		//���Ե�¼�Զ������漰�õ�CSS��ȡԪ��,������Ҫsleepһ��ʱ�䣬��ҳ�浯����û����ô��
		selenium.click("css=#u1 > a[name=\"tj_login\"]");
		
		Thread.sleep(20000);
		
		System.out.println("��ѡ���״̬"+selenium.getValue("id=TANGRAM__PSP_8__memberPass"));
		
		//selenium.waitForFrameToLoad("css=#u1", "a.name");;
		selenium.click("id=TANGRAM__PSP_8__userName");
		//selenium.click("xpath=//input[@name='username']");
		selenium.type("id=TANGRAM__PSP_8__userName", "�޹�waha�޹�");
		selenium.click("id=TANGRAM__PSP_8__password");
		selenium.type("id=TANGRAM__PSP_8__password", "peng2011");
		
		selenium.click("id=TANGRAM__PSP_8__memberPassWrapper");
		
		System.out.println("��ѡ���״̬"+selenium.getValue("id=TANGRAM__PSP_8__memberPass"));
		
		selenium.click("id=TANGRAM__PSP_8__submit");
	//	selenium.click(keyWordsLocator);
		Thread.sleep(50000);	
		selenium.click("id=kw");
		selenium.type("id=kw", "test");
		System.out.println(selenium.getValue("xpath=//input[@name='wd']"));
			
		selenium.click("id=su");
		//selenium.click(search);
		//selenium.waitForPageToLoad("50000");
		
		System.out.println("��ȡ������ı���"+selenium.getTitle());
		
		Thread.sleep(5000);	
		System.out.println("��ȡ������ı���"+selenium.getTitle());
		
	    //�ж�ҳ����ת�ǲ�����Ҫ��ҳ��
	    Assert.assertEquals(selenium.getTitle(), "test_�ٶ�����");
		//Assert.IsTrue(selenium.getTitle().contains("Google"));
	}

	@After
	public void tearDown() throws Exception {
		selenium.stop();
	}
}
