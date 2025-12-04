# Treasury Payments E2E Automation Framework

A robust, enterprise-grade End-to-End (E2E) automation framework designed for functional and integration testing of treasury payment systems (ACH, Wire, Positive Pay). Built with Python, Playwright, and Pytest, this framework supports UI, API, and E2E test suites, featuring data-driven testing, parallel cross-browser execution, and CI/CD integration via GitHub Actions.

## 🚀 Features

- **Modular Architecture:** Clear separation of concerns using Page Object Model (POM) for UI interactions, API client for backend testing, and dedicated test layers (UI, API, E2E).
- **Data-Driven Testing:** Utilizes YAML for external test data, enabling flexible and scalable test scenarios (e.g., varying limits, currencies, customer types, positive/negative cases).
- **Cross-Browser Compatibility:** Configured for parallel execution across Chromium and Firefox browsers using Playwright.
- **Continuous Integration (CI):** Integrated with GitHub Actions for automated test execution on every push and pull request, ensuring rapid feedback on code changes.
- **Environment Management:** Supports configurable test environments (e.g., Dev, QA, Production) via `.env` files and a centralized configuration utility.
- **Robust Reporting:** Generates detailed Playwright HTML reports for comprehensive test results and debugging.
- **Error Handling & Stability:** Implements strategies for handling flaky demo applications, including explicit `xfail` and `flaky` markers, to maintain CI stability.
- **Parallel Execution:** Leverages `pytest-xdist` for running tests in parallel, significantly reducing execution time.

## 🛠️ Technologies Used

- **Python 3.12+** - Primary programming language
- **Playwright** - Modern browser automation library
- **Pytest** - Test framework for structuring and running tests
- **PyYAML** - For loading data-driven test scenarios
- **python-dotenv** - For environment variable management
- **pytest-xdist** - For parallel test execution
- **pytest-playwright** - Pytest plugin for Playwright integration
- **GitHub Actions** - For CI/CD pipeline automation

## 📁 Project Structure

.
├── .github/
│ └── workflows/
│ └── playwright_ci.yml # GitHub Actions workflow for CI
├── data/
│ ├── login_cases.yaml # Example data for login scenarios
│ ├── ach_cases.yaml # Example data for ACH payment scenarios
│ └── transfer_scenarios.yaml # Example data for fund transfer scenarios
├── pages/ # Page Object Model (POM) classes
│ ├── base_page.py # Base page with common methods
│ ├── login_page.py # Login page objects (GlobalSQA)
│ ├── dashboard_page.py # Dashboard page objects
│ ├── pb_accounts_page.py # Parabank accounts page
│ ├── pb_transfer_page.py # Parabank transfer page
│ ├── pb_activity_page.py # Parabank activity page
│ └── ...
├── tests/
│ ├── api/ # API test suites (placeholder for payment APIs)
│ ├── e2e/ # End-to-End test suites
│ │ ├── test_data_driven_transfer.py
│ │ ├── test_globalsqa_flaky.py
│ │ ├── test_parabank_transfer.py
│ │ └── test_manager_navigation.py
│ └── ui/ # UI component test suites
│ └── test_login.py
├── utils/
│ ├── config.py # Configuration loader (reads from .env)
│ └── data_loader.py # Utility for loading YAML data
├── .env.example # Example environment variables
├── .gitignore # Git ignore file
├── conftest.py # Pytest fixtures and hooks
├── pytest.ini # Pytest configuration and custom markers
├── requirements.txt # Python dependencies
└── README.md # This file


## ⚙️ Setup and Installation

### Prerequisites

- Python 3.10 or higher
- Git
- pip (Python package manager)

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Farhod75/treasury-payments-e2e_python.git
   cd treasury-payments-e2e_python
Create and activate a virtual environment:

python -m venv venv

# On Windows:
.\venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
Install Python dependencies:
bash
Copy
pip install -r requirements.txt
Install Playwright browsers:

python -m playwright install chromium firefox
Configure environment variables:

# Copy the example .env file
cp .env.example .env

# Edit .env and populate with your configuration
# Example:
# BASE_URL=https://parabank.parasoft.com/parabank/index.htm
# GLOBALSQA_URL=https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login
🧪 Running Tests
Basic Test Execution

# Run all tests
pytest

# Run specific test file
pytest tests/e2e/test_parabank_transfer.py

# Run tests by marker
pytest -m "e2e"
pytest -m "e2e and not flaky"
pytest -m "regression"

# Run in headed mode (visible browser)
pytest --headed

# Run tests in parallel (faster execution)
pytest -n auto

# Run with verbose output
pytest -v
Generate Test Reports

# Generate Playwright HTML report
pytest --output=blob-report

# View the report (open in browser)
# The report will be in blob-report/index.html
Run Specific Browser

# Run on specific browser
pytest --browser chromium
pytest --browser firefox
pytest --browser webkit
🔄 CI/CD with GitHub Actions
This project includes a GitHub Actions workflow that automatically runs tests on every push and pull request.

Workflow Features:
Parallel Execution: Tests run in parallel across Chromium and Firefox browsers
Automated Browser Installation: Playwright browsers are installed automatically in the CI environment
Test Filtering: Only stable tests (marked as e2e and not flaky) are executed in CI
Artifact Upload: Playwright HTML reports are uploaded as artifacts for each browser
Viewing CI Results:
Navigate to the Actions tab in your GitHub repository
Click on the latest workflow run
View individual job results for Chromium and Firefox
Download Playwright report artifacts from the job summary (if available)
Workflow Configuration:
The CI workflow is defined in .github/workflows/playwright_ci.yml and runs on:

Push to main or master branches
Pull requests targeting main or master branches
📊 Test Markers
This framework uses custom Pytest markers to organize and filter tests:

Marker	Description
@pytest.mark.ui	UI component tests
@pytest.mark.api	API integration tests
@pytest.mark.e2e	End-to-End workflow tests
@pytest.mark.regression	Regression test suite
@pytest.mark.smoke	Smoke test suite
@pytest.mark.flaky	Tests that are flaky due to demo app instability
@pytest.mark.slow	Tests that take longer to execute
Example Usage:

# Run only E2E tests
pytest -m "e2e"

# Run regression tests excluding flaky ones
pytest -m "regression and not flaky"

# Run smoke tests only
pytest -m "smoke"
🎯 Data-Driven Testing
Test data is externalized in YAML files located in the data/ directory. This approach enables:

Easy maintenance of test scenarios
Separation of test logic from test data
Scalability for adding new test cases
Example: data/transfer_scenarios.yaml
yaml
Copy
- name: "valid_transfer_checking_to_savings"
  from_account_type: "CHECKING"
  to_account_type: "SAVINGS"
  amount: "10.00"
  expected_status: "Transfer Complete!"
  description: "Successful transfer from checking to savings."

- name: "invalid_transfer_negative_amount"
  from_account_type: "CHECKING"
  to_account_type: "SAVINGS"
  amount: "-5.00"
  expected_status: "Error"
  description: "Attempt to transfer a negative amount."
Tests can then be parameterized using this data:


@pytest.mark.parametrize("scenario", transfer_scenarios, ids=[s["name"] for s in transfer_scenarios])
def test_data_driven_transfer(scenario, ...):
    # Test implementation using scenario data
⚠️ Known Issues / Limitations
Demo Application Flakiness
This framework uses public demo applications (GlobalSQA Banking Project and Parabank) for demonstration purposes. These applications have known stability issues:

GlobalSQA: The "Add Customer" flow can be non-deterministic, with DOM elements not always appearing as expected.
Parabank: Account creation confirmation elements may not render consistently in headless mode.
Mitigation Strategies:
Test Markers: Flaky tests are marked with @pytest.mark.flaky and @pytest.mark.xfail to prevent CI failures.
CI Filtering: The CI pipeline excludes flaky tests using -m "e2e and not flaky".
Relaxed Assertions: Some assertions have been relaxed to focus on framework stability rather than demo app quirks.
Production Readiness:
For a real treasury payment system with stable backend services, this framework would provide:

Reliable E2E coverage
Comprehensive regression suites
Stable CI/CD integration
Full data-driven test scenarios
The current implementation demonstrates the framework's architecture and capabilities despite demo app limitations.

🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request
📝 License
This project is open source and available under the MIT License.

👤 Author
Farhod

GitHub: @Farhod75
LinkedIn: www.linkedin.com/in/farhod-elbekov-167324219
🙏 Acknowledgments
Demo applications used for testing:
GlobalSQA Banking Project
Parabank by Parasoft
Playwright for the excellent browser automation library
Pytest for the robust testing framework
Note: This is a portfolio/demonstration project. For production use with real treasury payment systems, additional security measures, authentication handling, and compliance considerations would be required.


