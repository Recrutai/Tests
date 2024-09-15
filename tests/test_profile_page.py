import pytest  
import time
from selenium import webdriver  
from selenium.webdriver.common.by import By
from uteis import get_variable

'''
    Testa o acesso as informações do perfil do usuário
'''

@pytest.fixture()  
def firefox_browser():  
    driver = webdriver.Firefox() 
    driver.implicitly_wait(5)
    yield driver
    driver.implicitly_wait(5)
    driver.quit()


def test_check_info_user_proflie(firefox_browser):
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
    profile_page = firefox_browser.find_element(By.XPATH,'//*[@id="main-content"]/header/form/div/a')
    profile_page.click()
    time.sleep(3)
    assert get_variable('VALIDE_EMAIL') in firefox_browser.page_source


def test_invalid_dada_in_experience(firefox_browser):
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
    profile_page = firefox_browser.find_element(By.XPATH,'//*[@id="main-content"]/header/form/div/a')
    profile_page.click()
    time.sleep(3)
    new_experience = firefox_browser.find_element(By.XPATH, '//*[@id="cardJobs"]/div[1]/div[2]/div')
    new_experience.click()
    submit_modal = firefox_browser.find_element(By.XPATH, '//*[@id="formJobs"]/div/button[1]')
    submit_modal.click()
    time.sleep(5)
    assert firefox_browser.switch_to.alert