import allure
import pytest
from config_loader import load_config

def pytest_addoption(parser):
    parser.addoption("--flow", action="store", default="sql_to_azure", help="Name of the flow to run")
    parser.addoption("--component", action="store", default="none", help="Component to execute")

@pytest.fixture
def flow(request):
    return request.config.getoption("--flow")

@pytest.fixture
def component(request):
    return request.config.getoption("--component")

@allure.suite("SQL to Azure Suite")
@allure.feature("SQL to Azure Workflow")
@pytest.mark.P1
def test_sql_to_azure(flow, component):
    with allure.step(f"Running flow: {flow}"):
        print(f"Running flow: {flow}")

    with allure.step(f"Running component: {component}"):
        print(f"Running component: {component}")

    # Load correct config dynamically
    e2e_flow_config = load_config(f'{flow}/e2eflow.yml')

    if component not in e2e_flow_config:
        pytest.fail(f"Component '{component}' not found in {flow}/e2eflow.yml")

    if e2e_flow_config[component]["enabled"]:
        with allure.step(f"{component} execution successful for {flow}"):
            print(f"{component} execution successful for {flow}")
    else:
        with allure.step(f"{component} execution skipped for {flow}"):
            print(f"{component} execution skipped for {flow}")




# if __name__ == "__main__":
#     try:
#         test_sql_to_azure()
#     except Exception as e:
#         print(f"Error: {e}")