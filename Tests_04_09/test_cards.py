import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_cards_search():
    driver = webdriver.Chrome(executable_path='C:\TestFiles_Selenium\chromedriver_win32\chromedriver.exe')
    #1. go to statsroyale.com
    driver.get('https://statsroyale.com')
    #2. go to cards page
    #driver.find_element(By.CSS_SELECTOR,'[href="/cards"]').click()
    #3. if acceptation of cookie needed
    # time.sleep(10)
    # driver.find_element(By.CSS_SELECTOR,"iframe[title='Accept']")   #$('[title="Accept"]')
    driver.switchTo().alert().accept();

    #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[title='Accept']"))).click()
    #driver.find_element(By.CLASS_NAME,'*message-button*')
    #driver.find_element(By.LINK_TEXT,'Accept')

    driver.close()