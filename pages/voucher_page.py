import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep
class VoucherPage(BasePage):
    BTN_ADD = (By.CSS_SELECTOR,"#__next > div:nth-child(2) > div:nth-child(4) > section > main > div.row.c-row > div.col-md-10 > div.status-container > div.status-white-container > div.rs-grid-container-fluid > div.VoucherManagerPage_is_bottom__Tfyph.show-grid.rs-row > div > button:nth-child(1)")
    FILE_BUTTON = (By.CSS_SELECTOR,"#form_check > div > div > div > div.rs-col.rs-col-sm-10.rs-col-xs-24 > div > div > div.is-mb.VoucherManagerPage_isflex__MdMPE.rs-row > div.rs-col.rs-col-xs-7 > div > div > div > input[type=file]")
    FILE_UPLOAD = "857681.png"
    TEXT_VOUCHER_NAME = (By.XPATH,"//*[@id='form_check']//div[@role='gridcell'][b[contains(.,'Tên chương trình ưu đãi')]]//input[@type='text']")
    TEXT_TITTLE = (By.XPATH,"//*[@id='form_check']//div[@role='gridcell'][b[contains(.,'Tiêu đề')]]//input[@type='text']")
    TEXT_HASHTAG = (By.XPATH,"//*[@id='form_check']//div[@role='gridcell'][b[contains(.,'Hashtag')]]//input[@type='text']")
    TEXT_ORIGINAL_PRICE = (By.XPATH,"//*[@id='form_check']//div[@role='gridcell'][b[contains(.,'Giá gốc')]]//input[@type='text']")
    TEXT_POINT_REQUIRED = (By.XPATH,"//*[@id='form_check']//div[@role='gridcell'][b[contains(.,'Số điểm đổi voucher')]]//input[@type='text']")
    TEXT_EXPIRED_DATE = (By.XPATH,"//*[@id='form_check']//div[@role='gridcell'][b[contains(.,'Thời gian code hết hạn')]]//input[@type='text']")
    TEXT_PREFIX = (By.XPATH,"//*[@id='form_check']//div[@role='gridcell'][b[contains(.,'Tiền tố mã')]]//input[@type='text']")
    TEXT_LOCATION = (By.XPATH,"//*[@id='form_check']//div[@role='gridcell'][b[contains(.,'Khu vực áp dụng')]]//input[@type='text']")
    PICKER_EXPIRED_DATE =  (By.XPATH,"//*[@id='form_check']//div[@role='gridcell'][b[contains(.,'Ngày code hết hạn')]]//div[@role='combobox']")
    TEXT_INFORMATION = (By.XPATH,"//*[@id='form_check']//div[@role='gridcell'][b[contains(.,'Mô tả chi tiết')]]//textarea")
    def add_voucher(self):
        self.find(self.BTN_ADD).click()
    def type_voucher_name(self,text):
        # self.scrollTo(self.TEXT_VOUCHER_NAME)
        self.type_text(self.TEXT_VOUCHER_NAME,text)
    def type_tittle(self,text):
        # self.scrollTo(self.TEXT_TITTLE)
        self.type_text(self.TEXT_TITTLE,text)
    def type_hashtag(self,text):
        # self.scrollTo(self.TEXT_HASHTAG)
        self.type_text(self.TEXT_HASHTAG,text)
    def type_original_price(self,text):
        # self.scrollTo(self.TEXT_ORIGINAL_PRICE)
        self.type_text(self.TEXT_ORIGINAL_PRICE,text)
    def type_point_required(self,text):
        # self.scrollTo(self.TEXT_POINT_REQUIRED)
        self.type_text(self.TEXT_POINT_REQUIRED,text)
    def type_expired_date(self,text):
        # self.scrollTo(self.TEXT_EXPIRED_DATE)
        self.type_text(self.TEXT_EXPIRED_DATE,text)
    def type_prefix(self,text):
        # self.scrollTo(self.TEXT_PREFIX)
        self.type_text(self.TEXT_PREFIX,text)
    def type_location(self,text):
        # self.scrollTo(self.TEXT_LOCATION)
        self.type_text(self.TEXT_LOCATION,text)
    def type_information(self,text):
        # self.scrollTo(self.TEXT_INFORMATION)
        self.type_text(self.TEXT_INFORMATION,text)
    def pick_expired_date(self,keys):
        # self.scrollTo(self.PICKER_EXPIRED_DATE)
        self.click(self.PICKER_EXPIRED_DATE)
        self.type_text(self.PICKER_EXPIRED_DATE,keys)
    def up_file(self):
        self.upload_file(self.FILE_BUTTON,self.FILE_UPLOAD)
    def fill_form(self,name,tittle,hashtag,price,point,ed,keys,prefix,location,information):
        self.add_voucher()
        self.up_file()
        self.type_voucher_name(name)
        self.type_tittle(tittle)
        self.type_hashtag(hashtag)
        self.type_original_price(price)
        self.type_point_required(point)
        self.type_expired_date(ed)
        # self.pick_expired_date(keys)
        self.type_prefix(prefix)
        self.type_location(location)
        self.type_information(information)