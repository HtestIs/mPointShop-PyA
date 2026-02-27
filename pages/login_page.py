from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.secure_area_page import SecureAreaPage
class LoginPage(BasePage):
    USER_NAME = (By.CSS_SELECTOR,"#__next > div.c-login-bg > div.c-login-box > div > div:nth-child(2) > input")
    PASSWORD_TEXT = (By.CSS_SELECTOR,"#__next > div.c-login-bg > div.c-login-box > div > div:nth-child(3) > input")
    BTTN = (By.CSS_SELECTOR,"#__next > div.c-login-bg > div.c-login-box > div > div.rs-btn-group > button")
    MESSAGE = (By.XPATH,"/html/body/div[3]/div[2]/div/div")
    def open(self):
        self.open_url("https://mpointshop.mediaone.dev/")
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
        return self.current_url()