from appium import webdriver
import os
# import time

CWD = os.getcwd()
HOST = 'http://localhost'
PORT = '4723'
APPIUM = 'http://localhost:4723/wd/hub'
APP_NAME = 'TheApp.app.zip'
FILEPATH = os.path.join(CWD, APP_NAME)
CAPS = {
    'platformName': 'iOS',
    'platformVersion': '14.5',
    'deviceName': 'iPhone Simulator',
    'automationName': 'XCUITest',
    'app': FILEPATH
}
driver = webdriver.Remote(command_executor=APPIUM, desired_capabilities=CAPS)
driver.quit()
dummy="123"
