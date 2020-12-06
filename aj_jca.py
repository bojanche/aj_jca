from selenium import webdriver
import os
import time


def open_browser(adresa, user, password):
    path = os.getcwd()+'\chromedriver.exe'
    options = webdriver.ChromeOptions()
    # ignores S&ST no-valid-cert on the camera
    options.add_argument('ignore-certificate-errors')
    # Various performance improvements
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-proxy-server")
    # keeps chrome open
    options.add_experimental_option('detach', True)
    # removes "Chrome is being controlled...blablabla" message
    options.add_experimental_option("excludeSwitches", ['enable-automation']);
    # full-screen mode for the app window
    options.add_argument("--kiosk")
    # Also I've added logging with -log switch...Same folder...
    browser = webdriver.Chrome(executable_path=path, options=options, service_args=["--verbose", "--log-path=chromedirver.log"])
    browser.get('https://'+adresa+':8443/?referrer=https%3A%2F%2F'+adresa+'%3A8443%2Fapp%2Fcom.tngtech.sastiot.feedback%2F')
    login_element = browser.find_element_by_id("Login_username")
    login_element.send_keys(user)
    password_element = browser.find_element_by_id("Login_password")
    password_element.send_keys(password)
    login_button = browser.find_element_by_id("Login_loginButton")
    login_button.click()
    time.sleep(60)
    browser.quit()


# The main executable
if __name__ == '__main__':
    while True:
        kamera_adresa = ''
        kamera_username = ''
        kamera_password = ''
        open_browser(kamera_adresa, kamera_username, kamera_password)
