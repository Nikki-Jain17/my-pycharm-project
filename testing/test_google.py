from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def test_google_search():
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # Run in headless mode
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    #
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    options = webdriver.EdgeOptions()
    options.add_argument('--headless')  # Run in headless mode
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)

    driver.get("https://www.google.com")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("GitHub Actions")
    search_box.submit()

    time.sleep(2)
    assert "GitHub" in driver.title

    driver.quit()
