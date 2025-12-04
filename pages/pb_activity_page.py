from playwright.sync_api import Page, expect
from .base_page import BasePage


class PbActivityPage(BasePage):
    """
    Parabank account activity page.
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.activity_rows = page.locator("#transactionTable tbody tr")

    def goto_activity_for_account(self, account_id: str):
        self.page.goto(f"{self.base_url.replace('index.htm','')}activity.htm?id={account_id}")
        expect(self.activity_rows.first).to_be_visible()

    def assert_has_transaction_with_amount(self, amount: str):
        row = self.activity_rows.filter(has_text=amount).first
        expect(row).to_be_visible()