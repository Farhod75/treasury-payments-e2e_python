import pytest
from playwright.sync_api import Page, Playwright, APIRequestContext
from typing import Dict, Any, Generator

from utils.config import config
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.gs_add_customer_page import AddCustomerPage
from pages.gs_open_account_page import OpenAccountPage
from pages.gs_customers_page import CustomersPage
from pages.pb_login_page import PbLoginPage
from pages.pb_accounts_page import PbAccountsPage
from pages.pb_transfer_page import PbTransferPage
from pages.pb_activity_page import PbActivityPage


@pytest.fixture(scope="session")
def api_client(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    """Fixture for API testing."""
    context = playwright.request.new_context(
        base_url=config.api_base_url,
        extra_http_headers={"Accept": "application/json"},
    )
    yield context
    context.dispose()


@pytest.fixture(scope="session")
def env_config() -> Dict[str, Any]:
    """Provides environment configuration."""
    return {
        "base_url": config.base_url,
        "api_base_url": config.api_base_url,
    }


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """Page object for the Login page (GlobalSQA)."""
    return LoginPage(page)


@pytest.fixture
def dashboard_page(page: Page) -> DashboardPage:
    """Page object for the Dashboard page (GlobalSQA)."""
    return DashboardPage(page)


@pytest.fixture
def authenticated_admin(login_page: LoginPage, dashboard_page: DashboardPage):
    """Logs in as Bank Manager (GlobalSQA) and returns the dashboard page."""
    login_page.goto()
    login_page.login_as_manager()
    dashboard_page.assert_loaded()
    return dashboard_page


@pytest.fixture
def add_customer_page(page: Page) -> AddCustomerPage:
    """Page object for the Add Customer page (GlobalSQA)."""
    return AddCustomerPage(page)


@pytest.fixture
def open_account_page(page: Page) -> OpenAccountPage:
    """Page object for the Open Account page (GlobalSQA)."""
    return OpenAccountPage(page)


@pytest.fixture
def customers_page(page: Page) -> CustomersPage:
    """Page object for the Customers page (GlobalSQA)."""
    return CustomersPage(page)


@pytest.fixture
def pb_login_page(page: Page) -> PbLoginPage:
    """Page object for Parabank login."""
    return PbLoginPage(page)


@pytest.fixture
def pb_accounts_page(page: Page) -> PbAccountsPage:
    """Page object for Parabank accounts."""
    return PbAccountsPage(page)


@pytest.fixture
def pb_transfer_page(page: Page) -> PbTransferPage:
    """Page object for Parabank transfer."""
    return PbTransferPage(page)


@pytest.fixture
def pb_activity_page(page: Page) -> PbActivityPage:
    """Page object for Parabank activity."""
    return PbActivityPage(page)


@pytest.fixture
def pb_authenticated_user(page: Page, pb_login_page: PbLoginPage):
    """
    Logs into Parabank and returns the logged-in page object context.
    Replace 'testuser' and 'testpass123' with your registered credentials.
    """
    pb_login_page.goto()
    pb_login_page.login("testuser", "testpass123")  # ← Use your registered username/password
    return page