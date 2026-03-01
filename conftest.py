import pytest
from driver_manager import DriverManager
from utils.logger import setup_logger
from utils.logger import test_filter
setup_logger()
@pytest.hookimpl(tryfirst=True)
def pytest_runtest_call(item):
    test_filter.test_name = item.name
@pytest.fixture
def driver():
    dm = DriverManager()
    driver = dm.get_driver()
    driver.maximize_window()
    yield driver
    driver.quit()
