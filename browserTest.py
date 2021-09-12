from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Location of chrome web driver stored in system
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

# Open URL
driver.get("https://python.org/")

# print title of web page
print(driver.title)

# close browser
driver.close()
