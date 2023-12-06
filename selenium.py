from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Path to your ChromeDriver executable
chrome_driver_path = ""C:\Users\admin\Downloads\chromedriver_win32""

# Initialize Chrome WebDriver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

try:
    # Open a website
    driver.get("https://www.example.com")

    # Perform some actions
    search_box = driver.find_element("name", "q")
    search_box.send_keys("Jenkins Selenium Integration")
    search_box.send_keys(Keys.RETURN)

    # Wait for a moment to see the result
    driver.implicitly_wait(5)

finally:
    # Close the browser window
    driver.quit()
