from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core import driver


def launch_browser():
    # Set up the ChromeDriver service using WebDriver Manager
    service = Service(ChromeDriverManager().install())
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome(service=service)
    # Open a website
    driver.get("https://www.google.com")
    # Optionally, maximize the window
    driver.maximize_window()
    return driver


def login():
    print('try')
