import pytest
import allure
from config_loader import load_config  # wherever your load_config is


@allure.suite("SQL to Azure Suite")
@allure.feature("SQL to Azure Workflow")
@pytest.mark.P1
def test_sql_to_azure(flow, component):
    with allure.step(f"Loading configuration for flow: {flow}"):
        e2e_flow_config = load_config(f'{flow}/e2eflow.yml')

    with allure.step(f"Validating component: {component}"):
        if component is None or component.lower() == "none":
            # If no specific component, run full E2E flow
            for comp_name, comp_details in e2e_flow_config.items():
                with allure.step(f"Running full E2E flow for component: {comp_name}"):
                    print(f"Executing full flow logic for component: {comp_name}")
                    # Add your execution logic here
        else:
            if component not in e2e_flow_config:
                # First attach the failure reason to Allure report
                allure.attach(
                    body=f"Component '{component}' not found in flow '{flow}'.",
                    name="Failure Reason",
                    attachment_type=allure.attachment_type.TEXT
                )
                # Then fail the test gracefully
                pytest.fail(f"Component '{component}' not found in {flow}/e2eflow.yml")

            if e2e_flow_config[component].get("enabled", False):
                with allure.step(f"Component '{component}' is enabled. Executing."):
                    print(f"{component} execution successful for {flow}")
                    # Insert your logic here
            else:
                with allure.step(f"Component '{component}' is disabled. Skipping execution."):
                    print(f"{component} execution skipped for {flow}")
