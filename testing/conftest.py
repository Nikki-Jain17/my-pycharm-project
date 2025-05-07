import os

import pytest
import allure
import logging
import io

# --------------- Setup basic logger ---------------- #
log_stream = io.StringIO()  # NEW: Create memory stream

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(log_stream)  # NEW: Log into memory
    ]
)
logger = logging.getLogger("pytest-logger")


# --------------- Pytest CLI Options ---------------- #
def pytest_addoption(parser):
    parser.addoption("--flow", action="store", default=None, help="Flow name")
    parser.addoption("--component", action="store", default=None, help="Component name")


@pytest.fixture
def flow(request):
    return request.config.getoption("--flow")

@pytest.fixture
def component(request):
    return request.config.getoption("--component")


# --------------- code for logging exceptions ---------------- #
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # Fetch flow and component
        flow_value = item.funcargs.get('flow', 'Unknown Flow')
        component_value = item.funcargs.get('component', 'Unknown Component')
        exception_info = str(call.excinfo.value)

        # Create a real log file
        log_content = (
            f"Test: {item.name}\n"
            f"Flow: {flow_value}\n"
            f"Component: {component_value}\n"
            f"Exception: {exception_info}\n"
        )

        log_filename = f"{item.name}_error_log.txt"
        log_filepath = os.path.join("allure-results", log_filename)  # Save it inside allure-results

        os.makedirs(os.path.dirname(log_filepath), exist_ok=True)
        with open(log_filepath, "w") as f:
            f.write(log_content)

        # Attach the real file to Allure
        with open(log_filepath, "rb") as f:
            allure.attach(
                f.read(),
                name="Failure_Log_File",
                attachment_type=allure.attachment_type.TEXT
            )

        # Also log in console
        logger.error(log_content)