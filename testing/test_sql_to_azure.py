import pytest
import allure
from config_loader import load_config  # wherever your load_config is


@allure.suite("SQL to Azure Suite")
@allure.feature("SQL to Azure Workflow")
@pytest.mark.P1
def test_sql_to_azure(flow, component):

    with allure.step(f"Running flow: {flow}"):
        print(f"Running flow: {flow}")

    with allure.step(f"Running component: {component}"):
        print(f"Running component: {component}")

    e2e_flow_config = load_config(f'{flow}/e2eflow.yml')

    if component is None or component == "none":
        # End-to-end mode: Run **all components** one by one
        for comp in e2e_flow_config:
            with allure.step(f"Running full E2E flow for component: {comp}"):
                print(f"Executing full flow logic for component: {comp}")
                # you can call your function to run component here
    else:
        if component not in e2e_flow_config:
            with allure.step(f"{component} not found * for {flow}"):
                pytest.fail(f"Component '{component}' not found in {flow}/e2eflow.yml")

        if e2e_flow_config[component]["enabled"]:
            with allure.step(f"{component} execution successful for {flow}"):
                print(f"{component} execution successful for {flow}")
                assert 2 + 2 == 5, "Math is wrong!"

        else:
            with allure.step(f"{component} execution skipped for {flow}"):
                print(f"{component} execution skipped for {flow}")