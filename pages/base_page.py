from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
import logging
import os
import time
class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
        self.logger = logging.getLogger(self.__class__.__name__)
        # self.actions = ActionChains(driver)
    def take_screenshot(self, name):
        path = f"screenshots/{name}.png"
        os.makedirs("screenshots", exist_ok=True)
        self.driver.save_screenshot(path)
        self.logger.info(f"Screenshot saved: {path}")
    def wait_presence(self,location):
        try:
            return self.wait.until(EC.presence_of_element_located(location))
        except Exception as e:
            self.logger.error(f"Element not present:{location}")
            self.take_screenshot(f"error_{int(time.time())}")
            self.logger.exception("Timeout while waiting for element")
            raise
    def wait_visible(self,location):
        try:
            return self.wait.until(EC.visibility_of_element_located(location))
        except Exception as e:
            self.logger.error(f"Element not visible:{location}")
            self.take_screenshot(f"error_{int(time.time())}")
            self.logger.exception("Timeout while waiting for element")
            raise
    def wait_clickable(self,location):
        try:
            return self.wait.until(EC.element_to_be_clickable(location))
        except Exception as e:
            self.logger.error(f"Element not clickable:{location}")
            self.take_screenshot(f"error_{int(time.time())}")
            self.logger.exception("Timeout while waiting for element")
            raise
    def open_url(self,url):
        self.logger.info(f"Navigating to {url}")
        self.driver.get(url)
    def find(self,location):
        try:
            element = self.wait_visible(location)
            return element
        except Exception as e:
            self.logger.error(f"Failed to find element:{location}")
            self.logger.exception(e)
            raise
    def click(self,location,retries=2):
        for i in range(retries):
            try:
                self.logger.info(f"Clicking element:{location}")
                element = self.wait_clickable(location)
                element.click()
                return
            except StaleElementReferenceException:
                self.logger.exception(f"Failed to click element:{location}, attempt{i+1}/{retries}")
                if i == retries - 1:
                    self.logger.exception(f"Failed after {retries} attempts for {location}")
                    raise
    def type_text(self,location,text,retries=2):
        for i in range(retries):
            try:
                self.logger.info(f"Typing info in element:{location} ")
                element= self.wait_clickable(location)
                element.clear()
                element.send_keys(text)
                return
            except StaleElementReferenceException:
                self.logger.exception(f"Failed to type at element: {location}")
                if i == retries-1:
                    raise
    def wait_url(self,url):
        self.wait.until(EC.url_changes(url))
    def current_url(self):
        return self.driver.current_url
    # def scrollTo(self,location):
    #     self.actions.move_to_element(self.find(location)).perform()
    # def send_key(self,location,keys):
    #     self.find(location).send_keys(keys)
    def upload_file(self,location,file_name):
        import os
        base_dir = os.getcwd()
        file_path = os.path.join(base_dir,"upload_file",file_name)
        self.find(location).send_keys(file_path)
    
    def assert_equal(self,actual_value,expected_value):
        if actual_value != expected_value:
            self.logger.error(f"Assertion Failed | Expected: {expected_value} | Actual: {actual_value}")
            raise AssertionError(f"Expected:{expected_value}| Actual: {actual_value}")
        else:
            self.logger.info("Assertion passed")