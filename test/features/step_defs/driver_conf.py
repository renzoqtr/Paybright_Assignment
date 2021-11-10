import os

from selenium import webdriver


def get_chromedriver_path():
    stream = os.popen('which chromedriver')
    return stream.read().strip()


def get_geckodriver_path():
    stream = os.popen('which geckodriver')
    return stream.read().strip()


def init_driver(driver_name="FIREFOX"):
    if driver_name == "FIREFOX":
        driver = webdriver.Firefox(executable_path=get_geckodriver_path())
    if driver_name == "CHROME":
        driver = webdriver.Chrome(executable_path=get_chromedriver_path())
    return driver
