import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function", autouse=True)
def driver():
    """Setup WebDriver and quit after each test."""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    service = Service()  # Use auto-detection for chromedriver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()

def test_add_to_cart(driver):
    """Test adding an item to the cart."""
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.find_element(By.XPATH, "//*[text()='Brocolli - 1 Kg']/parent::div//button").click()
    driver.find_element(By.XPATH, "//a[@class='cart-icon']//img").click()
    time.sleep(2)  # Small delay to verify cart update

def pytest_runtest_makereport(item, call):
    """Take a screenshot if test fails."""
    if call.when == "call" and call.excinfo is not None:
        driver = item.funcargs["driver"]
        screenshot_path = f"screenshots/{item.name}.png"
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved: {screenshot_path}")
