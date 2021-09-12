import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://demo.guru99.com/test/newtours/")
print(driver.title)  # 1

driver.get("http://pavantestingtools.blogspot.in/")
print(driver.title)  # 2
time.sleep(5)

driver.back()
time.sleep(5)
print(driver.title)  # 1

driver.forward()
time.sleep(5)
print(driver.title)  # 2
