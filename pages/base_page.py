from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
        # self.actions = ActionChains(driver)
    def wait_visible(self,location):
        self.wait.until(EC.visibility_of_element_located(location))
    def wait_clickable(self,location):
        self.wait.until(EC.element_to_be_clickable(location))
    def open_url(self,url):
        self.driver.get(url)
    def find(self,location):
        return self.driver.find_element(*location)
    def click(self,location):
        self.wait_clickable(location)
        element = self.find(location)
        element.click()
    def type_text(self,location,text):
        self.wait_clickable(location)
        element = self.find(location)
        element.clear()
        element.send_keys(text)
    def wait_url(self,url):
        self.wait.until(EC.url_contains(url))
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