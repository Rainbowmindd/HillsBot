from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#chrome config
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")


driver=webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)

driver.get("https://hillswear.com/pl")

WebDriverWait(driver, 1)

try:
    WebDriverWait(driver, 30).until(
        lambda d: d.execute_script('return document.readyState') == 'complete'
    )
    #debugging
    print(driver.page_source)

    cookies_button=WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CLASS_NAME,"shopify-pc__banner__btn-accept"))
    )
    cookies_button.click()

#waiting for search icon
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.no-style.fire-search"))
    )

    #search_button.click()
    driver.execute_script("arguments[0].scrollIntoView(true);", search_button)

    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.no-style.fire-search"))
    )

    driver.execute_script("arguments[0].click();", search_button)
    print("Dupa.")

    search_box=WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "q"))
    )
    search_box.click()
    print("Dupa.2")
    search_box.send_keys("T Shirt")
    print("Dupa3") #dotad dziala


except TimeoutException as e:
    print("Loading took too long")
finally:
    time.sleep(20)
    driver.quit()

