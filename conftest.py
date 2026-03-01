import pytest
from driver_manager import DriverManager
from utils.logger import setup_logger
from utils.logger import test_filter
import time
import logging
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
logger = logging.getLogger(__name__)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call(item):
    start_time = time.time()
    logger.info(f"===== START TEST: {item.name} =====")
    outcome = yield
    duration = time.time() - start_time
    logger.info(f"===== END TEST: {item.name} | Duration: {duration:.2f}s =====")
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call":
        if result.failed:
            logger.error(f"===== TEST FAILED: {item.name} =====")
        elif result.passed:
            logger.info(f"===== TEST PASSED: {item.name} =====")