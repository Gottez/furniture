import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


search_query = "Techno"


@pytest.fixture(scope="module")
def chrome_driver():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    url = "https://radiothek.orf.at/search"
    driver.get(url)
    expectation = EC.presence_of_element_located((By.CSS_SELECTOR, "#didomi-notice-agree-button"))
    element = WebDriverWait(driver, 10).until(expectation)
    element.click()

    yield driver
    driver.quit()


def test_fall1(chrome_driver):

    search_element = chrome_driver.find_element(By.CSS_SELECTOR, ".search-input")
    submit_element = chrome_driver.find_element(By.CSS_SELECTOR, ".icon")

    search_element.send_keys(search_query)

    submit_element.click()

    result_is_present = EC.presence_of_element_located((By.CSS_SELECTOR, ".results-title"))
    result_header_element = WebDriverWait(chrome_driver, 10).until(result_is_present)

    assert result_header_element.text == f'Suchergebnis für "{search_query}"'


def test_fall2(chrome_driver):

    suche = chrome_driver.find_elements(By.CSS_SELECTOR, ".type")
    s1_dict = {}

    for i in suche:
        if i.text in s1_dict:
            s1_dict[i.text] += 1
        else:
            s1_dict[i.text] = 1
        print(s1_dict)
        assert len(s1_dict) >= 1


#def test_fall3(chrome_driver):

    #suche3 = chrome_driver.find_elements(By.CSS_SELECTOR, "#dropdown-nwx72-label")
    #suche3.click()

    #suche4 = chrome_driver.find_elements(By.CSS_SELECTOR, "#dropdown-u6oza-results-oe1")
    #suche4.click()







