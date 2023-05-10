from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import time


class Crawler(object):

    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_url(self, url):
        self.driver.get(url)

    def get_element(self, xpath, wait_time=3):
        try:
            element = WebDriverWait(self.driver, wait_time).until(
                ec.presence_of_element_located((By.XPATH, xpath)))
        except Exception as e:
            print("Got error finding xpath %s: %s" % (xpath, e))
            element = None
        return element

    def get_elements(self, xpath, wait_time=10):
        try:
            elements = WebDriverWait(self.driver, wait_time).until(
                ec.presence_of_all_elements_located((By.XPATH, xpath)))
        except Exception as e:
            print("Got error finding xpath %s: %s" % (xpath, e))
            elements = list()
        return elements

    def get_element_text(self, xpath):
        text = ""
        element = self.get_element(xpath)
        if element is not None:
            text = element.text
        return text

    def send_input(self, xpath, text):
        element = self.get_element(xpath)
        element.send_keys(text)
        time.sleep(1)
        element.send_keys(Keys.ENTER)
        time.sleep(1)

