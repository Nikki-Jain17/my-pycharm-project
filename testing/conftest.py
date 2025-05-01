

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
