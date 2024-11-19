import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_login():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
    chrome_options.add_argument("--window-size=1920x1080")  # Set screen size for the headless mode
    driver = webdriver.Chrome(options=chrome_options)
    # driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    # Locate elements and perform actions
    driver.find_element(By.ID, "username").send_keys("rahulshettyacademy")
    driver.find_element(By.NAME, "password").send_keys("learning")
    driver.find_element(By.XPATH, "//input[@name='signin']").click()
    time.sleep(3)
    # Check if login was successful by checking the page title
    assert "ProtoCommerce" in driver.title

    driver.close()