from playwright.sync_api import Page
from .base_page import BasePage


class LoginPage(BasePage):
    """
    Landing page of GlobalSQA Banking Project.
    Provides entry to Bank Manager and Customer login flows.
    """

    def __init__(self, page: Page):
        super().__init__(page)
        # No base_url arg; BasePage already set self.base_url
        # keep your locators here
        # Buttons on the landing/login page
        self.manager_login_button = page.get_by_role("button", name="Bank Manager Login")
        self.customer_login_button = page.get_by_role("button", name="Customer Login")

    def goto(self):
        # Explicitly navigate to the login hash route
        self.page.goto(f"{self.base_url}/#/login")

    def login_as_manager(self):
        self.manager_login_button.click()

    def go_to_customer_login(self):
        self.customer_login_button.click()