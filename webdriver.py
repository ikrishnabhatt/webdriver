from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH="C:\Users\KRISH\Downloads\chromedriver_win32"

driver = webdriver.Chrome(PATH)
driver.get("https://www.espncricketinfo.come/scores")

# Open the website
driver.get("https://www.espncricketinfo.come/scores")

# Wait for an element with a specific ID to be visible
element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "element_id"))
)

# Click on an element by ID
element = driver.find_element_by_id("element_id")
element.click()

# Find an input field by ID and type text into it
input_field = driver.find_element_by_id("input_field_id")
input_field.send_keys("Text to type")

# Take a screenshot and save it to a file
driver.save_screenshot("screenshot.png")

# Store the current window handle
current_window = driver.current_window_handle

# Perform an action that opens a new window or tab

# Switch to the new window or tab
driver.switch_to.window(driver.window_handles[-1])

# Navigating back to the previous page
driver.back()

# Navigating forward to the next page
driver.forward()

# Set the browser window size to a specific width and height
driver.set_window_size(800, 600)

# Handling Dropdown Menus
dropdown = Select(driver.find_element_by_id("dropdown_id"))
dropdown.select_by_visible_text("Option Text")

# Execute JavaScript code
driver.execute_script("alert('Hello, World!');"

# Scroll to a specific element on the page
element = driver.find_element_by_id("element_id")
driver.execute_script("arguments[0].scrollIntoView(true);", element)

# Wait for the page title to contain a specific text
WebDriverWait(driver, 10).until(EC.title_contains("Page Title"))

# Wait for an element to be clickable
element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "element_id")))


# Close the browser
driver.quit()