from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://demoqa.com/automation-practice-form")
time.sleep(2)

# Close ad banner if it appears
try:
    driver.execute_script("document.querySelector('#close-fixedban').click()")
except:
    pass

# -- Personal Information (customized) --
first_name = "Aaron"
last_name = "Jones"
email = "aaron.jones.dev@gmail.com"
phone = "4802134567"
address = "4321 Lambeezy Lane, Phoenix, AZ 85004"

# Fill First & Last Name
driver.find_element(By.ID, "firstName").send_keys(first_name)
driver.find_element(By.ID, "lastName").send_keys(last_name)

# Fill Email
driver.find_element(By.ID, "userEmail").send_keys(email)

# Select Gender
driver.find_element(By.XPATH, "//label[contains(text(),'Male')]").click()

# Fill Phone Number
driver.find_element(By.ID, "userNumber").send_keys(phone)

# Scroll down to view more elements
driver.execute_script("window.scrollBy(0, 300);")

# Close date picker popup
driver.find_element(By.ID, "dateOfBirthInput").send_keys(Keys.ESCAPE)

# Fill Subject
subject_input = driver.find_element(By.ID, "subjectsInput")
subject_input.send_keys("Computer Science")
subject_input.send_keys(Keys.RETURN)

# Check Hobby
driver.find_element(By.XPATH, "//label[contains(text(),'Reading')]").click()

# Fill Address
driver.find_element(By.ID, "currentAddress").send_keys(address)

# Select State and City
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element(By.ID, "react-select-3-input").send_keys("NCR")
driver.find_element(By.ID, "react-select-3-input").send_keys(Keys.RETURN)

driver.find_element(By.ID, "react-select-4-input").send_keys("Delhi")
driver.find_element(By.ID, "react-select-4-input").send_keys(Keys.RETURN)

# Submit
driver.find_element(By.ID, "submit").click()
time.sleep(2)

# Screenshot result
driver.save_screenshot("form_submission_result.png")

driver.quit()
