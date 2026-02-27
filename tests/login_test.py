from time import sleep

from pages.login_page import LoginPage
import pytest

@pytest.fixture
def goToURL(driver):
    login = LoginPage(driver)
    login.open()
    return login
def test_valid_login(goToURL):
    goToURL.login("craftmbeer_1","123456789")
    assert "/merchant-scan/voucher" in goToURL.getURL()

@pytest.mark.parametrize("username,password,expected",[
    ("abc","acx","Cửa hàng không tồn tại!"),
    ("craftmbeer_1","abc","Thông tin đăng nhập tài khoản không đúng. Xin vui lòng thử lại sau !"),
    ("","","Vui lòng điền các trường còn thiếu!")
])
def test_invalid(goToURL,username,password,expected):
    goToURL.login(username,password)
    assert expected in goToURL.getMessage()
    # print(goToURL.getMessage())