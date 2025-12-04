import pytest
import time


@pytest.mark.e2e
@pytest.mark.regression
def test_parabank_open_account_only(pb_authenticated_user, pb_accounts_page):
    """
    Minimal stable E2E:
    - Login
    - Go to Open New Account
    - Create account
    - Verify newAccountId is shown
    """
    new_account_id = pb_accounts_page.open_new_account(account_type="CHECKING")
    assert new_account_id and new_account_id.strip() != ""
    time.sleep(1)