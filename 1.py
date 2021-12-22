
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

browser = webdriver.Chrome()
browser.get("https://accounts.spotify.com/tr/login?continue=https://open.spotify.com/user/76ck031tz84tb9inafu2a49u1")
with open("hesaplar.txt") as f:
	for line in f:
		linedata = line.split(':')
		username = browser.find_element_by_id("login-username")
		password = browser.find_element_by_id("login-password")
		username.send_keys(linedata[0])
		password.send_keys(linedata[1])
		password.send_keys(Keys.ENTER)
		time.sleep(8)
		button = browser.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[3]/main/div[2]/div[2]/div/div/div[2]/section/div/div[3]/div/button[1]')
		button.click()
		time.sleep(2)
		
		
		
		
        
		
	
		try:
			browser.find_element_by_xpath("/html/body/div[2]/div/form/div[1]/div/p/span")
			browser.find_element_by_id("login-username").clear()
			browser.find_element_by_id("login-password").clear()
			print("Error in login")
		except NoSuchElementException:
			print(linedata[0])
			print(linedata[1])
			browser.close()
			browser = webdriver.Chrome()
			browser.get("https://accounts.spotify.com/tr/login?continue=https://open.spotify.com/user/76ck031tz84tb9inafu2a49u1")
			
			
          