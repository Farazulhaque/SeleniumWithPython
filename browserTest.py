from selenium import webdriver

# Location of chrome web driver stored in system
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")             # Chrome
# driver = webdriver.Firefox(executable_path="C:\Drivers\geckodriver-v0.29.1\geckodriver.exe")          # Firefox
# driver = webdriver.Ie(executable_path="C:\Drivers\IEDriverServer_Win32_3.150.2\IEDriverServer.exe")   # Internet
# Explorer driver = webdriver.Edge(executable_path="C:\Drivers\edgedriver_win64\msedgedriver.exe        # Microsoft Edge


# Open URL
driver.get("https://farazulhaque.github.io/weatherappproject/")

# print title of web page
print(driver.title)

# print current url
print(driver.current_url)

# get page source
print(driver.page_source)

# close browser
driver.close()
