from playwright.sync_api import Page, expect
from .base_page import BasePage


class PbLoginPage(BasePage):
    """
    Parabank login page.
    """

    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = page.locator("input[name='username']")
        self.password_input = page.locator("input[name='password']")
        self.login_button = page.locator("input[value='Log In']")

    def goto(self):
        self.page.goto(self.base_url)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        # After login, we should see 'Accounts Overview' link
        expect(self.page.locator("a[href*='overview.htm']")).to_be_visible()