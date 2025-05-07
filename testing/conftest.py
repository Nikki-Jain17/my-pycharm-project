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
        # Fetching flow and component safely
        flow_value = item.funcargs.get('flow', 'Unknown Flow')
        component_value = item.funcargs.get('component', 'Unknown Component')

        # Attach captured logs
        log_contents = log_stream.getvalue()
        if log_contents:
            allure.attach(log_contents, name="Captured Logs", attachment_type=allure.attachment_type.TEXT)

        # Only on failure, attach exception info
        if report.failed:
            exception_info = str(call.excinfo.value)

            with allure.step(f"Failure in test: {item.name}"):
                allure.attach(
                    f"Flow: {flow_value}\nComponent: {component_value}\nException: {exception_info}",
                    name="Failure Details",
                    attachment_type=allure.attachment_type.TEXT
                )

            # Log the error properly
            logger.error(f"Test '{item.name}' failed")
            logger.error(f"Flow: {flow_value}")
            logger.error(f"Component: {component_value}")
            logger.error(f"Exception: {exception_info}")

        # Clear the log_stream for next test
        log_stream.truncate(0)
        log_stream.seek(0)
