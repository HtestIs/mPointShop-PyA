from pages.secure_area_page import SecureAreaPage
from pages.voucher_page import VoucherPage
from pages.login_page import LoginPage
from time import sleep
import pytest

@pytest.fixture
def login_page(driver):
    login_valid = LoginPage(driver)
    login_valid.open()
    secure = login_valid.login("mbeer_partner","123456789")
    voucher = secure.go_to_voucher_page()
    voucher.wait_url("/manager/voucher-manager")
    return voucher
# def test_assert_url(login_page):
#     assert "/manager/voucher-manager" in login_page.current_url()
    # print(login_page.current_url())
def test_fill_form(login_page):
    login_page.fill_form("name","title","hashtag","12","50000","180","10/05/2026","prefix","location","information")
    sleep(5)