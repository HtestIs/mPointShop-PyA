import pytest
from driver_manager import DriverManager
from utils.logger import setup_logger
from utils.logger import test_filter
import time
from datetime import datetime
import logging
import os
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
@pytest.hookimpl()
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
def pytest_configure(config):
    if not os.path.exists("reports"):
        os.makedirs("reports")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_file = f"reports/report_{timestamp}.html"
    config.option.htmlpath = report_file
    if config.pluginmanager.hasplugin("html"):
        config._metadata = getattr(config, "_metadata", {})
        config._metadata["Project Name"] = "MPOINTSHOP"
        config._metadata["Tester"] = "Hieu"
        config._metadata["Environment"] = "Chrome"
        config.option.htmlpath = report_file
def pytest_html_report_title(report):
    report.title = "MPOINTSHOP Automation Report"
