from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, \
    invisibility_of_element_located, presence_of_all_elements_located

# classe que contém as funções globais.

class Global_Page():

    def __init__(self, driver):
        self.driver = driver

    def find_all(self, *locator):
        return WebDriverWait(self.driver, timeout).until(presence_of_all_elements_located(*locator))

    def find(self, *locator):
        return WebDriverWait(self.driver, timeout).until(visibility_of_element_located(*locator))

    def find_not(self, *locator):
        return WebDriverWait(self.driver, timeout).until(invisibility_of_element_located(*locator))

    def tearDown(self):
        self.driver.quit()