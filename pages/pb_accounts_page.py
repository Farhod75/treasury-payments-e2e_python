import re
from playwright.sync_api import Page, expect
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
        self.page.goto(self.base_url.replace("index.htm", "overview.htm"))
        expect(self.page).to_have_url(re.compile(".*overview\\.htm"))

    def open_new_account(self, account_type: str = "CHECKING") -> str:
        self.open_new_account_link.click()
        expect(self.page).to_have_url(re.compile(".*openaccount\\.htm"))

        self.new_account_type_select.select_option(account_type)
        # Use first existing account as funding source if present; otherwise index 0 is fine
        self.new_account_from_select.select_option(index=0)
        self.new_account_button.click()

        # Confirmation page: account id appears with id 'newAccountId'
        expect(self.new_account_id_link).to_be_visible()
        new_account_id = self.new_account_id_link.inner_text().strip()
        return new_account_id