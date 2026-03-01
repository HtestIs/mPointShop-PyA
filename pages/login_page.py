from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.secure_area_page import SecureAreaPage
class LoginPage(BasePage):
    USER_NAME = (By.CSS_SELECTOR,"#__next > div.c-login-bg > div.c-login-box > dixv > div:nth-child(2) > input")
    PASSWORD_TEXT = (By.CSS_SELECTOR,"#__next > div.c-login-bg > div.c-login-box > div > div:nth-child(3) > input")
    BTTN = (By.CSS_SELECTOR,"#__next > div.c-login-bg > div.c-login-box > div > div.rs-btn-group > button")
    MESSAGE = (By.XPATH,"//div[@role='alert']//div[normalize-space()]")
    URL= "https://mpointshop.mediaone.dev/login"
    def open(self):
        self.open_url(self.URL)
    def enterUsername(self,text):
        self.type_text(self.USER_NAME,text)
    def enterPassword(self,text):
        self.type_text(self.PASSWORD_TEXT,text)
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