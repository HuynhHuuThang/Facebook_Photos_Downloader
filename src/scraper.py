from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from dotenv import load_dotenv
load_dotenv()

# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--enable-unsafe-webgl")

# launch the Chrome WebDriver 
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def facebook_login():
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
    time.sleep(5)

def scraper(element_class_name):
    

    # Extract Images URLs
    # Navigate to the specified Facebook page
    driver.get("https://web.facebook.com/Gaixinh24h.tv/photos")
    time.sleep(5)  # Wait for the page to load
    # html_source = driver.page_source
    # with open("page_source.html", "w", encoding="utf-8") as f:  # UTF-8 encoding is important
    #   f.write(html_source) # Or f.write(element_html) or f.write(element_outer_html)

    
    for element in photos_elements:
        with open("element_urls.txt", "a") as f:
            f.write(element.get_attribute("src") + "\n")
    time.sleep(10)
async def fnd_element(element_class_name):
    photos_elements = []
    photos_elements = driver.find_elements(By.CLASS_NAME, element_class_name)
    


element_class_name = "x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g x1sur9pj xkrqix3 x1s688f x1lliihq x5yr21d x1n2onr6 xh8yej3"
scraper(element_class_name)
