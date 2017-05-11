#coding=utf-8
"""
This example shows how to find the elements. Use trademe as an example
"""

from selenium import webdriver

url = "http://www.trademe.co.nz"
driver = webdriver.Chrome()
print "Opening Chrome"
driver.get(url)

#find the login button by ID
loginBtn = driver.find_element_by_id("LoginLink")
#click the login button
loginBtn.click()
print "login page is displayed"

#find the email field by name page_email
email = driver.find_element_by_name("page_email")
email.click()

#

