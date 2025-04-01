import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_open_google():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    # Manually provide ChromeDriver path
    #service = Service("C:/Users/adijain17/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)



    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    driver.find_element(By.XPATH,"//*[text()='Brocolli - 1 Kg']/parent::div//button").click()
    driver.find_element(By.XPATH, "//a[@class='cart-icon']//img").click()
    time.sleep(5)
    driver.quit()

test_open_google()



