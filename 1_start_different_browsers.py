#coding=utf-8

from selenium import webdriver
import time

url = "http://www.trademe.co.nz"
#Start Chrome
driver = webdriver.Chrome()
print "Opening Chrome"
#Access the url in Chrome
driver.get(url)
#wait 3 seconds
time.sleep(3)
#quit the browser
driver.quit()

#Start Firefox
driver = webdriver.Firefox()
print "Opening Firefox"
#Access the url in Firefox
driver.get(url)
#wait 3 seconds
time.sleep(3)
#quit the browser
driver.quit()

