from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://demo.guru99.com/test/newtours/")

user_ele = driver.find_element_by_name("userName")

print(user_ele.is_displayed())  # return true/false based on element status
print(user_ele.is_enabled())  # return true/false

pwd_ele = driver.find_element_by_name("password")
print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())

user_ele.send_keys("mercury")
pwd_ele.send_keys("mercury")

driver.find_element_by_name("submit").click()  # click submit button

driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr/td["
                             "1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/a").click()  # click
# Flights link

roundtrip_radio = driver.find_element_by_css_selector("input[value=roundtrip]")
print(f"Status of roundtrip radio button: {roundtrip_radio.is_selected()}")  # print status of roundtrip radio button

onewaytrip_radio = driver.find_element_by_css_selector("input[value=oneway]")
print(f"Status of onewaytrip radio button: {onewaytrip_radio.is_selected()}")

driver.close()
