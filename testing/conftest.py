import os
import traceback

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

        exception_type = type(call.excinfo.value).__name__
        exception_message = str(call.excinfo.value)
        stack_trace = ''.join(traceback.format_exception(None, call.excinfo.value, call.excinfo.tb))

        # Prepare log content
        failure_details = (
            f"Flow: {flow_value}\n"
            f"Component: {component_value}\n"
            f"Exception Type: {exception_type}\n"
            f"Exception Message: {exception_message}\n\n"
            f"Stack Trace:\n{stack_trace}"
        )

        # Attach to Allure
        with allure.step(f"Failure in test: {item.name}"):
            allure.attach(
                failure_details,
                name="Failure_Log_File",
                attachment_type=allure.attachment_type.TEXT
            )

        # Also log into console (or pytest captured logs)
        logger.error(f"Test '{item.name}' failed")
        logger.error(failure_details)

