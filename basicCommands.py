import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")

print(driver.title)  # returns title of the page

print(driver.current_url)  # returns URL of the page

driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()

time.sleep(5)

# driver.close()        # Close currently focussed browser
driver.quit()  # Close all browser
