from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set up the WebDriver
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Find the search bar element
search_box = driver.find_element("name", "q")

# Type the search query
search_box.send_keys("Selenium WebDriver")

# Submit the search form
search_box.send_keys(Keys.RETURN)

# Wait for the results to load
driver.implicitly_wait(5)

# Print the title of the page
print(driver.title)

# Close the browser
driver.quit()
