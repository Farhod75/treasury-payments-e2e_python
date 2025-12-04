from playwright.sync_api import Page, expect
from .base_page import BasePage


class DashboardPage(BasePage):
    """
    Bank Manager dashboard page for GlobalSQA Banking Project.
    """

    def __init__(self, page: Page):
        super().__init__(page)
        # Unique elements visible only on the manager dashboard
        self.add_customer_button = page.get_by_role("button", name="Add Customer")
        self.open_account_button = page.get_by_role("button", name="Open Account")
        self.customers_button = page.get_by_role("button", name="Customers")

    def assert_loaded(self):
        # URL changes to manager view
        self.wait_for_url_contains("#/manager")
        expect(self.add_customer_button).to_be_visible()
        expect(self.open_account_button).to_be_visible()
        expect(self.customers_button).to_be_visible()