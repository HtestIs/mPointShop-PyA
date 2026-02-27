import pytest
from driver_manager import DriverManager

@pytest.fixture
def driver():
    dm = DriverManager()
    driver = dm.get_driver()
    driver.maximize_window()
    yield driver
    driver.quit()