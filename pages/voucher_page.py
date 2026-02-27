from selenium.webdriver.common.by import By
from pages.base_page import BasePage
class VoucherPage(BasePage):
    BTN_ADD = (By.CSS_SELECTOR,"#__next > div:nth-child(2) > div:nth-child(4) > section > main > div.row.c-row > div.col-md-10 > div.status-container > div.status-white-container > div.rs-grid-container-fluid > div.VoucherManagerPage_is_bottom__Tfyph.show-grid.rs-row > div > button:nth-child(1)")
    TEXT_VOUCHER_NAME = (By.CSS_SELECTOR,"#form_check > div > div > div > div.rs-col.rs-col-sm-10.rs-col-xs-24 > div > div > div.is-mb.VoucherManagerPage_isflex__MdMPE.rs-row > div.rs-col.rs-col-xs-14 > input")
    TEXT_TITTLE = {By.CSS_SELECTOR,"#form_check > div > div > div > div.rs-col.rs-col-sm-10.rs-col-xs-24 > div > div > div:nth-child(3) > div:nth-child(1) > input"}
    TEXT_HASHTAG = {By.CSS_SELECTOR,"#form_check > div > div > div > div.rs-col.rs-col-sm-10.rs-col-xs-24 > div > div > div:nth-child(3) > div:nth-child(2) > input"}
    TEXT_ORIGINAL_PRICE = {By.CSS_SELECTOR,"#form_check > div > div > div > div.rs-col.rs-col-sm-10.rs-col-xs-24 > div > div > div:nth-child(4) > div:nth-child(1) > input"}
    TEXT_POINT_REQUIRED = {By.CSS_SELECTOR,"#form_check > div > div > div > div.rs-col.rs-col-sm-10.rs-col-xs-24 > div > div > div:nth-child(4) > div:nth-child(2) > input"}
    TEXT_EXPIRED_DATE = {By.CSS_SELECTOR,"#form_check > div > div > div > div.rs-col.rs-col-sm-10.rs-col-xs-24 > div > div > div:nth-child(5) > div:nth-child(1) > div > input"}
    TEXT_PREFIX = {By.CSS_SELECTOR,"#form_check > div > div > div > div.rs-col.rs-col-sm-10.rs-col-xs-24 > div > div > div:nth-child(6) > div:nth-child(1) > input"}
    TEXT_LOCATION = {By.CSS_SELECTOR,"#form_check > div > div > div > div.rs-col.rs-col-sm-10.rs-col-xs-24 > div > div > div:nth-child(7) > div:nth-child(1) > input"}
    TEXT_INFORMATION = {By.CSS_SELECTOR,"#form_check > div > div > div > div.rs-col.rs-col-sm-10.rs-col-xs-24 > div > div > div:nth-child(8) > div > textarea"}
    PICKER_EXPIRED_DATE = {By.CSS_SELECTOR,"#form_check > div > div > div > div.rs-col.rs-col-sm-10.rs-col-xs-24 > div > div > div:nth-child(5) > div:nth-child(2) > div > div"}
    def add_voucher(self):
        self.find(self.BTN_ADD).click()
    def type_voucher_name(self,text):
        self.scrollTo(self.TEXT_VOUCHER_NAME)
        self.type_text(self.TEXT_VOUCHER_NAME,text)
    def type_tittle(self,text):
        self.scrollTo(self.TEXT_TITTLE)
        self.type_text(self.TEXT_TITTLE,text)
    def type_hashtag(self,text):
        self.scrollTo(self.TEXT_HASHTAG)
        self.type_text(self.TEXT_HASHTAG,text)
    def type_original_price(self,text):
        self.scrollTo(self.TEXT_ORIGINAL_PRICE)
        self.type_text(self.TEXT_ORIGINAL_PRICE,text)
    def type_point_required(self,text):
        self.scrollTo(self.TEXT_POINT_REQUIRED)
        self.type_text(self.TEXT_POINT_REQUIRED,text)
    def type_expired_date(self,text):
        self.scrollTo(self.TEXT_EXPIRED_DATE)
        self.type_text(self.TEXT_EXPIRED_DATE,text)
    def type_prefix(self,text):
        self.scrollTo(self.TEXT_PREFIX)
        self.type_text(self.TEXT_PREFIX,text)
    def type_location(self,text):
        self.scrollTo(self.TEXT_LOCATION)
        self.type_text(self.TEXT_LOCATION,text)
    def type_information(self,text):
        self.scrollTo(self.TEXT_INFORMATION)
        self.type_text(self.TEXT_INFORMATION,text)
    def pick_expired_date(self,keys):
        self.scrollTo(self.PICKER_EXPIRED_DATE)
        self.click(self.PICKER_EXPIRED_DATE)
        self.send_key(self.PICKER_EXPIRED_DATE,keys)
    def fill_form(self,name,tittle,hashtag,price,point,ed,keys,prefix,location,information):
        self.add_voucher()
        self.type_voucher_name(name)
        self.type_tittle(tittle)
        # self.type_hashtag(hashtag)
        # self.type_original_price(price)
        # self.type_point_required(point)
        # self.type_expired_date(ed)
        # self.pick_expired_date(keys)
        # self.type_prefix(prefix)
        # self.type_location(location)
        # self.type_information(information)