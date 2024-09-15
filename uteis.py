import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from dotenv import load_dotenv

load_dotenv()

def get_variable(key):
    return str(os.getenv(key))


def fill_select_input(driver, css_selector, value):
    element = Select(driver.find_element(By.CSS_SELECTOR, css_selector))
    element.select_by_visible_text(value)
    time.sleep(2)
