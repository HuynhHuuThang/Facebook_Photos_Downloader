from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.wesdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from dotenv import load_dotenv
load_dotenv()

def scraper():
    # Set up Selenium WebDriver
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    # launch the Chrome WebDriver 
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    # open facebook login page
    driver.get("https://www.facebook.com/login")

    # login credentials authen
    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")

    email_imput = driver.find_element(By.ID, "email")
    password_imput = driver.find_element(By.ID, "pass")
    email_imput.send_keys(EMAIL)
    password_imput.send_keys(PASSWORD)
    password_imput.send_keys(Keys.RETURN)

    time.sleep(10)
