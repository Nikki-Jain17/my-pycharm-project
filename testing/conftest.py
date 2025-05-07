import pytest
import allure

def pytest_addoption(parser):
    parser.addoption("--flow", action="store", default=None, help="Flow name")
    parser.addoption("--component", action="store", default=None, help="Component name")

import pytest

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

        exception_info = str(call.excinfo.value)

        with allure.step(f"Failure in test: {item.name}"):
            allure.attach(
                f"Flow: {flow_value}\nComponent: {component_value}\nException: {exception_info}",
                name="Failure Details",
                attachment_type=allure.attachment_type.TEXT
            )

        print(f"[ERROR] Test '{item.name}' failed")
        print(f"Flow: {flow_value}")
        print(f"Component: {component_value}")
        print(f"Exception: {exception_info}")
