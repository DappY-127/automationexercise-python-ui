import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function", autouse=True)
def browser(request):
    download_folder = os.path.join(os.getcwd(), 'pages', 'resources')
    
    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-setuid-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--start-maximized")
    options.add_argument('--window-size=1920,1080')

    preferences = {"download.default_directory": download_folder}
    options.add_experimental_option("prefs", preferences)

    browser = webdriver.Chrome(options=options)
    request.cls.driver = browser
    yield browser
    browser.close()
    browser.quit()