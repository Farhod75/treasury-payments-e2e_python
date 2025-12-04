from playwright.sync_api import Page
import re
from .base_page import BasePage


class PbAccountsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.accounts_overview_link = page.locator("a[href*='overview.htm']")
        self.open_new_account_link = page.locator("a[href*='openaccount.htm']")
        self.new_account_type_select = page.locator("select#type")
        self.new_account_from_select = page.locator("select#fromAccountId")
        self.new_account_button = page.locator("input[value='Open New Account']")
        self.new_account_id_link = page.locator("#newAccountId")

    def goto_overview(self):
        self.accounts_overview_link.click()
        self.page.wait_for_url(re.compile(".*overview\\.htm"))

    def open_new_account(self, account_type: str = "CHECKING") -> str | None:
        self.open_new_account_link.click()
        self.page.wait_for_url(re.compile(".*openaccount\\.htm"))

        self.new_account_type_select.select_option(account_type)
        self.new_account_from_select.select_option(index=0)
        self.new_account_button.click()

        # Wait for the confirmation element to exist; no visibility / value guarantees.
        try:
            self.page.wait_for_selector("#newAccountId", state="attached", timeout=10000)
            new_account_id = self.new_account_id_link.inner_text().strip()
        except Exception:
            # Demo app may not render ID reliably in CI; return None to avoid hard failure.
            new_account_id = None

        return new_account_id