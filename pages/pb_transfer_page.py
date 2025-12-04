from playwright.sync_api import Page, expect
from .base_page import BasePage
import re


class PbTransferPage(BasePage):
    """
    Parabank 'Transfer Funds' functionality.
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.transfer_funds_link = page.locator("a[href*='transfer.htm']")
        self.amount_input = page.locator("input#amount")
        self.from_account_select = page.locator("select#fromAccountId")
        self.to_account_select = page.locator("select#toAccountId")
        self.transfer_button = page.locator("input[value='Transfer']")
        self.transfer_result = page.locator("#rightPanel .title")  # e.g. 'Transfer Complete!'

    def goto_transfer(self):
        self.transfer_funds_link.click()
        expect(self.page).to_have_url(re.compile(".*transfer\\.htm"))

    def transfer(self, amount: str, from_account: str, to_account: str):
        self.amount_input.fill(amount)
        self.from_account_select.select_option(from_account)
        self.to_account_select.select_option(to_account)
        self.transfer_button.click()
        expect(self.transfer_result).to_have_text("Transfer Complete!")