import pytest  
import time
from selenium import webdriver  
from selenium.webdriver.common.by import By
from uteis import get_variable, fill_select_input

'''
    Testa as funcionalidades ligadas ao usuário recrutador.
'''

@pytest.fixture()  
def firefox_browser():  
    driver = webdriver.Firefox() 
    driver.implicitly_wait(5)
    yield driver
    driver.implicitly_wait(5)
    driver.quit()


def test_test_vacancy_registration_with_invalid_data(firefox_browser):
    index_page_url = get_variable('INDEX_PAGE_URL')
    firefox_browser.get(index_page_url)
    login_button = firefox_browser.find_element(By.XPATH, "/html/body/main/div/div[1]/a")
    login_button.click()
    email = firefox_browser.find_element(By.CSS_SELECTOR, '#email')
    email.send_keys(get_variable('VALIDE_EMAIL'))
    password = firefox_browser.find_element(By.CSS_SELECTOR, '#password')
    password.send_keys(get_variable('VALIDE_PASSWORD'))
    submit = firefox_browser.find_element(By.XPATH, '/html/body/div/form/button')
    submit.click()
    time.sleep(5)
    open_modal = firefox_browser.find_element(By.CSS_SELECTOR, '#openModalBtn')
    open_modal.click()
    submit_vacancy_button = firefox_browser.find_element(By.CSS_SELECTOR, '#vacancyForm > button')
    submit_vacancy_button.click()
    time.sleep(5)
    assert firefox_browser.switch_to.alert


def test_test_vacancy_registration_with_valid_data(firefox_browser):
    index_page_url = get_variable('INDEX_PAGE_URL')
    firefox_browser.get(index_page_url)
    login_button = firefox_browser.find_element(By.XPATH, "/html/body/main/div/div[1]/a")
    login_button.click()
    email = firefox_browser.find_element(By.CSS_SELECTOR, '#email')
    email.send_keys(get_variable('VALIDE_EMAIL'))
    password = firefox_browser.find_element(By.CSS_SELECTOR, '#password')
    password.send_keys(get_variable('VALIDE_PASSWORD'))
    submit = firefox_browser.find_element(By.XPATH, '/html/body/div/form/button')
    submit.click()
    time.sleep(5)
    open_modal = firefox_browser.find_element(By.CSS_SELECTOR, '#openModalBtn')
    open_modal.click()
    title = firefox_browser.find_element(By.CSS_SELECTOR, '#title')
    title.send_keys('*VACANCY*')
    description = firefox_browser.find_element(By.CSS_SELECTOR, '#description')
    description.send_keys('VACANCY DESCRIPTION')
    fill_select_input(firefox_browser, '#institutionId', 'Cesar')
    fill_select_input(firefox_browser, '#employmentType', 'Freelancer')
    fill_select_input(firefox_browser, '#workModel', 'Presencial')
    fill_select_input(firefox_browser, '#states-Select', 'Pernambuco')
    time.sleep(5)
    fill_select_input(firefox_browser, '#cities-Select', 'Recife')
    salary = firefox_browser.find_element(By.CSS_SELECTOR, '#salary')
    salary.send_keys('1000')
    positions = firefox_browser.find_element(By.CSS_SELECTOR, '#positions')
    positions.send_keys('1')
    time.sleep(3)
    submit_vacancy_button = firefox_browser.find_element(By.CSS_SELECTOR, '#vacancyForm > button')
    submit_vacancy_button.click()
    time.sleep(5)
    assert '*VACANCY*' in firefox_browser.page_source
