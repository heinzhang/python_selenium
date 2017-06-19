#coding=utf-8
"""
This example shows how to find the elements. Use trademe as an example
"""

from selenium import webdriver
import time

url = "http://www.trademe.co.nz"
driver = webdriver.Chrome()
print "Opening Chrome"
driver.get(url)

#find the login button by ID
loginBtn = driver.find_element_by_id("LoginLink")
#click the login button
loginBtn.click()
print "login page is displayed"
time.sleep(3)

#find the email field by name page_email 
email_tbx = driver.find_element_by_name("page_email")

#input your email address
email = "DO NOT USE THIS@EMAIL.ADDRESS"
#Replace the password with your own password
pwd = "DO NOT USE THIS PASSWORD" 
email_tbx.send_keys(email)

#find the password field by name page_password
pwd_tbx = driver.find_element_by_name("page_password")
pwd_tbx.send_keys(pwd)

#find the login button by class name
loginBtn2 = driver.find_element_by_class_name("spriteButton\ button27")
#click the login button
loginBtn2.click()

driver.close()
