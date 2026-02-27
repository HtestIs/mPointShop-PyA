from selenium import webdriver
from selenium.webdriver.chrome.options import Options
class DriverManager:
    def get_driver(self):
        prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2
        }
        options = Options()
        options.add_experimental_option("prefs",prefs)
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-save-password-bubble")
        options.add_argument("--disable-infobars")
        options.add_argument("--guest")
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(5)
        return driver