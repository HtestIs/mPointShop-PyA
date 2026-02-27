from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.voucher_page import VoucherPage
class SecureAreaPage(BasePage):
    VOUCHER = (By.XPATH,"/html/body/div[3]/div[1]/div[4]/section/main/div/div[2]/div[1]/div[4]")
    CLOSE_MODAL = (By.CSS_SELECTOR,"#dialog-19 > div > div > div.rs-modal-header > span")
    def close_modal(self):
        self.click(self.CLOSE_MODAL)
    def go_to_voucher_page(self):
        self.click(self.VOUCHER)
        return VoucherPage(self.driver)

