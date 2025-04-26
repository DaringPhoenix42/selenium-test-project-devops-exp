from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup ChromeDriver automatically using WebDriverManager
service_obj = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service_obj)

# Maximize window
driver.maximize_window()

# Open Google
driver.get("https://www.google.com")

# Find search box
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("javatpoint")
search_box.send_keys(Keys.RETURN)

# Wait for 3 seconds
time.sleep(3)

# Close the browser
driver.quit()
