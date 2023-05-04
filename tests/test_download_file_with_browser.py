import os.path
import time
from zipfile import ZipFile

from selenium import webdriver
from selene import browser
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from conftest import TMP_PATH


# TODO оформить в тест, добавить ассерты и использовать универсальный путь к tmp

def test_download_file_with_browser():
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": TMP_PATH,
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)

    browser.config.driver_options = options

    browser.open("https://github.com/pytest-dev/pytest")
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()
    time.sleep(5)

    with ZipFile(os.path.join(TMP_PATH, 'pytest-main.zip')) as pytestzip:
        pytestzip_content = list(pytestzip.namelist())
        assert 'pytest-main/setup.py' in pytestzip_content

