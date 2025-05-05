import pytest
import allure
from config_loader import load_config  # wherever your load_config is
from _pytest.fixtures import FixtureRequest

def run_component_logic(flow, component):
    print(f"Executing real logic for {component} inside {flow} flow")
    # Place actual call here

@allure.suite("SQL to Azure Suite")
@allure.feature("SQL to Azure Workflow")
@pytest.mark.P1
def test_sql_to_azure(request: FixtureRequest):
    flow = request.config.getoption("--flow")
    component = request.config.getoption("--component")

    with allure.step(f"Running flow: {flow}"):
        print(f"Running flow: {flow}")

    with allure.step(f"Running component: {component}"):
        print(f"Running component: {component}")

    e2e_flow_config = load_config(f'{flow}/e2eflow.yml')

    if not component or component.lower() == "none":
        for comp in e2e_flow_config:
            if e2e_flow_config[comp]["enabled"]:
                with allure.step(f"Running full E2E flow for component: {comp}"):
                    print(f"Executing full E2E flow logic for component: {comp}")
                    run_component_logic(flow, comp)
            else:
                print(f"Skipping disabled component: {comp}")
    else:
        if component not in e2e_flow_config:
            pytest.fail(f"Component '{component}' not found in {flow}/e2eflow.yml")

        if e2e_flow_config[component]["enabled"]:
            print(f"Exact Running component: {component}")
            run_component_logic(flow, component)

            with allure.step(f"{component} execution successful for {flow}"):
                print(f"{component} execution successful for {flow}")
        else:
            with allure.step(f"{component} execution skipped for {flow}"):
                print(f"{component} execution skipped for {flow}")
