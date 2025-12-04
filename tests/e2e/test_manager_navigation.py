import pytest
import time

@pytest.mark.e2e
@pytest.mark.flaky(reason="GlobalSQA navigation can be intermittently slow")
@pytest.mark.xfail(reason="Demo app instability - excluded from CI", strict=False)
def test_manager_can_navigate_tabs(authenticated_admin, page):
    # Just prove we can use all three tabs without relying on flaky behavior
    page.get_by_role("button", name="Add Customer").click()
    time.sleep(0.5)
    page.get_by_role("button", name="Open Account").click()
    time.sleep(0.5)
    page.get_by_role("button", name="Customers").click()
    time.sleep(0.5)