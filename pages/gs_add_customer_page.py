from playwright.sync_api import Page
from .base_page import BasePage


class AddCustomerPage(BasePage):
    """
    Page Object for the 'Add Customer' functionality in the Bank Manager section.
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.add_customer_tab = page.get_by_role("button", name="Add Customer").nth(0)
        self.first_name_input = page.get_by_placeholder("First Name")
        self.last_name_input = page.get_by_placeholder("Last Name")
        self.post_code_input = page.get_by_placeholder("Post Code")
        # The submit button inside the form
        self.submit_button = page.get_by_role("button", name="Add Customer").nth(1)

    def goto_add_customer_form(self):
        self.add_customer_tab.click()
        self.wait_for_url_contains("#/manager/addCust")

    def add_customer(self, first_name: str, last_name: str, post_code: str):
        """Fill form, click submit, and accept the alert exactly once."""
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.post_code_input.fill(post_code)

        # Expect exactly one dialog triggered by the click
        with self.page.expect_event("dialog") as dialog_info:
            self.submit_button.click()
        dialog = dialog_info.value
        dialog.accept()