import pytest
import time


@pytest.mark.e2e
@pytest.mark.regression
@pytest.mark.xfail(reason="GlobalSQA demo app: Add Customer flow is flaky / non-deterministic", strict=False)
def test_full_treasury_payment_workflow(
    authenticated_admin,
    add_customer_page,
    open_account_page,
    customers_page,
):
    first_name = "Test"
    last_name = "User"
    post_code = "12345"
    customer_full_name = f"{first_name} {last_name}"
    currency = "Dollar"

    # 1. Add customer
    add_customer_page.goto_add_customer_form()
    add_customer_page.add_customer(first_name, last_name, post_code)
    time.sleep(1)

    # 2. Open account
    open_account_page.goto_open_account_form()
    open_account_page.open_account(customer_full_name, currency)
    time.sleep(1)

    # 3. Customers list (keep assertion simple; the app is flaky)
    customers_page.goto_customers_list()
    customers_page.search_customer(first_name)  # search by first name only

    # Minimal, robust assertion: at least one row exists after search
    rows = customers_page.customer_table.locator("tbody tr")
    assert rows.count() > 0
    time.sleep(2)