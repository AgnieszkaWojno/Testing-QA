#1. pip install pytest
#2. Settings->Tools->Python Integrated Tools      Testing->Default: pytest

#dla testów automatycznych:
#3. pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_google_search():
    print('wow')
    driver = webdriver.Chrome(executable_path='C:\TestFiles_Selenium\chromedriver_win32\chromedriver.exe')
    #driver = webdriver #.Chrome()

    # # 1. go to google.com
    driver.get('https://google.com')
    # # # 2. type in a search 'puppies'
    driver.find_element(By.ID,'L2AGLb').click()
    driver.find_element(By.NAME, 'q').send_keys('puppies')
    # # 3. submit or enter the search
    driver.find_element(By.NAME,'btnK').submit()
    # # 4. assert we go a search for puppies
    print(driver.title)
    print(driver.current_url)
    assert 'puppies' in driver.title          #assert - zapewnić/ dowieść czegoś /  szukaj słowa 'puppies' w tytule strony