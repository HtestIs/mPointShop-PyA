import logging
import os
class TestNameFilter(logging.Filter):
    def __init__(self):
        super().__init__()
        self.test_name = "GLOBAL"

    def filter(self, record):
        record.test_name = self.test_name
        return True

test_filter = TestNameFilter()
def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(test_name)s | %(name)s | %(message)s",
        handlers=[
            logging.FileHandler("automation.log", mode="w", encoding="utf-8"),
            logging.StreamHandler()
        ],
        force=True
    )

    root_logger = logging.getLogger()

    for handler in root_logger.handlers:
        handler.addFilter(test_filter)