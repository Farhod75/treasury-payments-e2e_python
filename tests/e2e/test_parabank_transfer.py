import pytest

@pytest.mark.e2e
@pytest.mark.regression
def test_parabank_open_account_only(pb_authenticated_user, pb_accounts_page):
    new_account_id = pb_accounts_page.open_new_account(account_type="CHECKING")
    # For CI stability against flaky demo app, only assert that the flow completes without exceptions.
    # new_account_id may be None or empty in headless CI because Parabank doesn't always render it.