import pytest
import allure
from config_loader import load_config
import logging

logger = logging.getLogger("pytest-logger")

@allure.suite("SQL to Azure Suite")
@allure.feature("SQL to Azure Workflow")
@pytest.mark.P1
def test_sql_to_azure(flow, component):

    with allure.step(f"Running flow: {flow}"):
        logger.info(f"Running flow: {flow}")

    with allure.step(f"Running component: {component}"):
        logger.info(f"Running flow: {flow}")

    e2e_flow_config = load_config(f'{flow}/e2eflow.yml')

    if component is None or component == "none":
        # End-to-end mode: Run **all components** one by one
        for comp in e2e_flow_config:
            with allure.step(f"Running full E2E flow for component: {comp}"):
                logger.info(f"Executing full flow logic for component: {comp}")
                # you can call your function to run component here
    else:
        if component not in e2e_flow_config:
            with allure.step(f"{component} not found * for {flow}"):
                logger.error(f"Component '{component}' not found in {flow}/e2eflow.yml")
                pytest.fail(f"Component '{component}' not found in {flow}/e2eflow.yml")

        if e2e_flow_config[component]["enabled"]:
            with allure.step(f"{component} execution successful for {flow}"):
                logger.info(f"{component} execution successful for {flow}")
                result = 10 / 0  # Will raise ZeroDivisionError naturally

        else:
            with allure.step(f"{component} execution skipped for {flow}"):
                logger.warning(f"{component} execution skipped for {flow}")