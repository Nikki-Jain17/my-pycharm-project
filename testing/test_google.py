from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_google_search():
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # Run in headless mode
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')

    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Edge()
    driver.get("https://www.google.com")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("GitHub Actions")
    search_box.submit()

    time.sleep(2)
    assert "GitHub" in driver.title

    driver.quit()
