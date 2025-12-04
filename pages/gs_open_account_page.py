from playwright.sync_api import Page
from .base_page import BasePage


class OpenAccountPage(BasePage):
    """
    Page Object for the 'Open Account' functionality in the Bank Manager section.
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.open_account_tab = page.get_by_role("button", name="Open Account")
        self.customer_select = page.locator("#userSelect")
        self.currency_select = page.locator("#currency")
        self.process_button = page.get_by_role("button", name="Process")

    def goto_open_account_form(self):
        self.open_account_tab.click()
        self.wait_for_url_contains("#/manager/openAccount")

    def open_account(self, customer_name: str, currency: str):
        """Open account and accept the alert exactly once."""
        self.customer_select.select_option(label=customer_name)
        self.currency_select.select_option(label=currency)

        with self.page.expect_event("dialog") as dialog_info:
            self.process_button.click()
        dialog = dialog_info.value
        dialog.accept()