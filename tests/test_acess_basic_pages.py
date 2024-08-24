import pytest  
from selenium import webdriver  
from selenium.webdriver.common.by import By
from uteis import get_variable
'''
    Testa o acesso básico as páginas de Index, Login e Registro
'''

@pytest.fixture()  
def firefox_browser():  
    driver = webdriver.Firefox() 
    driver.implicitly_wait(5)
    yield driver
    driver.implicitly_wait(5)
    driver.quit()


def test_index_page(firefox_browser):

    url = get_variable('HOME_PAGE_URL')
    firefox_browser.get(url)
    main_content = '''
      O Recrutaí é um sistema web que auxilia os estudantes de instituições
      públicas e privadas a serem recrutados para estágios e projetos de
      pesquisa e extensão.
    '''
    assert main_content in firefox_browser.page_source


def test_login_page_redirect(firefox_browser):

    home_page_url = get_variable('HOME_PAGE_URL')
    login_page_url = get_variable('LOGIN_PAGE_URL')
    firefox_browser.get(home_page_url)
    login_button = firefox_browser.find_element(By.XPATH, "/html/body/main/div/div[1]/a")
    login_button.click()
    assert login_page_url == firefox_browser.current_url


def test_register_page_redirect(firefox_browser):

    home_page_url = get_variable('HOME_PAGE_URL')
    register_page_url = get_variable('REGISTER_PAGE_URL')
    firefox_browser.get(home_page_url)
    login_button = firefox_browser.find_element(By.XPATH, "/html/body/main/div/div[2]/a")
    login_button.click()
    assert register_page_url == firefox_browser.current_url

