from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://demo.guru99.com/test/newtours/")

driver.implicitly_wait(10)  # wait for 10 seconds after executing above steps

assert "Welcome: Mercury Tours" in driver.title

user_ele = driver.find_element_by_name("userName").send_keys("mercury")
pwd_ele = driver.find_element_by_name("password").send_keys("mercury")
driver.find_element_by_name("submit").click()  # click submit button
