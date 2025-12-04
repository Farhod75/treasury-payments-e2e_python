import re
from playwright.sync_api import Page, expect
from utils.config import config


class BasePage:
    """
    Base page object with common utilities.
    """

    def __init__(self, page: Page):
        self.page = page
        self.base_url = config.base_url

    def wait_for_url_contains(self, fragment: str, timeout: int = 5000):
        """Wait for the URL to contain a specific fragment."""
        pattern = re.compile(re.escape(fragment))
        expect(self.page).to_have_url(pattern, timeout=timeout)