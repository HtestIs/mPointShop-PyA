from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.secure_area_page import SecureAreaPage
from utils.decorators import step
class LoginPage(BasePage):
    USER_NAME = (By.CSS_SELECTOR,"#__next > div.c-login-bg > div.c-login-box > div > div:nth-child(2) > input")
    PASSWORD_TEXT = (By.CSS_SELECTOR,"#__next > div.c-login-bg > div.c-login-box > div > div:nth-child(3) > input")
    BTTN = (By.CSS_SELECTOR,"#__next > div.c-login-bg > div.c-login-box > div > div.rs-btn-group > button")
    MESSAGE = (By.XPATH,"//div[@role='alert']//div[normalize-space()]")
    URL= "https://mpointshop.mediaone.dev/login"
    @step("Open login page")
    def open(self):
        self.open_url(self.URL)
    @step("Enter Username")
    def enterUsername(self,text):
        self.type_text(self.USER_NAME,text)
    @step("Enter password")
    def enterPassword(self,text):
        self.type_text(self.PASSWORD_TEXT,text)
    @step("Click login button")
    def clickButton(self):
        self.click(self.BTTN)
        return SecureAreaPage(self.driver)
    def login(self,userName,passWord):
        self.enterUsername(userName)
        self.enterPassword(passWord)
        return self.clickButton()
    def getMessage(self):
        self.wait_visible(self.MESSAGE)
        return self.find(self.MESSAGE).text
    def getURL(self):
        self.wait_url(self.URL)
        return self.current_url()