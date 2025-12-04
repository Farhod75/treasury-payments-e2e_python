from playwright.sync_api import Page, expect
from .base_page import BasePage


class CustomersPage(BasePage):
    """
    Page Object for the 'Customers' functionality in the Bank Manager section.
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.customers_tab = page.get_by_role("button", name="Customers")
        self.search_customer_input = page.get_by_placeholder("Search Customer")
        self.customer_table = page.locator("table.table")

    def goto_customers_list(self):
        self.customers_tab.click()
        self.wait_for_url_contains("#/manager/list")

    def search_customer(self, search_term: str):
        self.search_customer_input.fill(search_term)

    def assert_customer_in_list(self, first_name: str, last_name: str, post_code: str | None = None):
        """
        Assert that some row exists whose first three cells are:
        [First Name, Last Name, Post Code].
        """
        rows = self.customer_table.locator("tbody tr")

        # Find the first row whose first td has first_name
        row = rows.filter(
            has=self.page.locator("td:nth-child(1)", has_text=first_name)
        ).first

        # Row must exist
        expect(row).to_be_visible()

        # Now assert the other columns relative to that row
        first_td = row.locator("td").nth(0)
        last_td = row.locator("td").nth(1)
        post_td = row.locator("td").nth(2)

        expect(first_td).to_have_text(first_name)
        expect(last_td).to_have_text(last_name)
        if post_code:
            expect(post_td).to_have_text(post_code)