import pytest  
import time
from selenium import webdriver  
from selenium.webdriver.common.by import By
from uteis import get_variable
'''
    Testa o acesso básico as páginas de Index, Login, Logout Registro
'''

@pytest.fixture()  
def firefox_browser():  
    driver = webdriver.Firefox() 
    driver.implicitly_wait(5)
    yield driver
    driver.implicitly_wait(5)
    driver.quit()


def test_index_page(firefox_browser):

    url = get_variable('INDEX_PAGE_URL')
    firefox_browser.get(url)
    main_content = '''
      O Recrutaí é um sistema web que auxilia os estudantes de instituições
      públicas e privadas a serem recrutados para estágios e projetos de
      pesquisa e extensão.
    '''
    assert main_content in firefox_browser.page_source


def test_login_page_redirect(firefox_browser):

    index_page_url = get_variable('INDEX_PAGE_URL')
    login_page_url = get_variable('LOGIN_PAGE_URL')
    firefox_browser.get(index_page_url)
    login_button = firefox_browser.find_element(By.XPATH, "/html/body/main/div/div[1]/a")
    login_button.click()
    assert login_page_url == firefox_browser.current_url


def test_register_page_redirect(firefox_browser):

    index_page_url = get_variable('INDEX_PAGE_URL')
    register_page_url = get_variable('REGISTER_PAGE_URL')
    firefox_browser.get(index_page_url)
    register_button = firefox_browser.find_element(By.XPATH, "/html/body/main/div/div[2]/a")
    register_button.click()
    assert register_page_url == firefox_browser.current_url


def test_login_page_invalid_credential(firefox_browser):
    index_page_url = get_variable('INDEX_PAGE_URL')
    firefox_browser.get(index_page_url)
    login_button = firefox_browser.find_element(By.XPATH, "/html/body/main/div/div[1]/a")
    login_button.click()
    email = firefox_browser.find_element(By.CSS_SELECTOR, '#email')
    email.send_keys('test@gmail.com')
    password = firefox_browser.find_element(By.CSS_SELECTOR, '#password')
    password.send_keys('password')
    submit = firefox_browser.find_element(By.XPATH, '/html/body/div/form/button')
    submit.click()
    time.sleep(5)
    assert 'Login ou Senha Inválidos' in firefox_browser.page_source


def test_login_success(firefox_browser):
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
    home_page_url = get_variable('HOME_PAGE_URL')
    assert home_page_url in firefox_browser.current_url


def test_register_with_invalid_data(firefox_browser):
    index_page_url = get_variable('INDEX_PAGE_URL')
    firefox_browser.get(index_page_url)
    register_button = firefox_browser.find_element(By.XPATH, "/html/body/main/div/div[2]/a")
    register_button.click()
    submit_button = firefox_browser.find_element(By.CSS_SELECTOR, '#registerForm > button')
    submit_button.click()
    time.sleep(5)
    assert firefox_browser.switch_to.alert


def test_register_user_sucess(firefox_browser):
    index_page_url = get_variable('INDEX_PAGE_URL')
    firefox_browser.get(index_page_url)
    register_button = firefox_browser.find_element(By.XPATH, "/html/body/main/div/div[2]/a")
    register_button.click()
    submit_button = firefox_browser.find_element(By.CSS_SELECTOR, '#registerForm > button')
    first_name = firefox_browser.find_element(By.XPATH, '//*[@id="firstName"]')
    first_name.send_keys("Henrique")
    last_name = firefox_browser.find_element(By.XPATH, '//*[@id="lastName"]')
    last_name.send_keys("Venancio")
    head_line = firefox_browser.find_element(By.XPATH, '//*[@id="headline"]')
    head_line.send_keys("Frontend")
    city = firefox_browser.find_element(By.XPATH, '//*[@id="city"]')
    city.send_keys("Recife")
    email = firefox_browser.find_element(By.XPATH, '//*[@id="email"]')
    email.send_keys("hvs@gmail.com")
    password = firefox_browser.find_element(By.XPATH, '//*[@id="password"]')
    password.send_keys("Henrique@123")
    submit_button.click()
    time.sleep(5)
    code_verif_page = get_variable("VERIFICATION_PAGE_URL")
    assert code_verif_page in firefox_browser.current_url


def test_acess_home_page_not_logged(firefox_browser):
    home_page = get_variable('HOME_PAGE_URL')
    firefox_browser.get(home_page)
    login_page_url = get_variable('LOGIN_PAGE_URL')
    assert login_page_url in firefox_browser.current_url