import pytest
import allure

@allure.suite("SQL to Azure Suite")
@allure.feature("SQL to Azure Workflow")
@pytest.mark.P1
class TestSQLToAzure:

    @allure.story("Register Physical Dataset")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sql_to_azure
    @pytest.mark.register_physical_dataset
    def test_register_physical_dataset_sql(self):
        with allure.step("Running SQL to Azure - register_physical_dataset"):
            print("Running SQL to Azure - register_physical_dataset")
        assert True

    @allure.story("Register Virtual Dataset")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sql_to_azure
    @pytest.mark.register_virtual_dataset
    def test_register_virtual_dataset_sql(self):
        with allure.step("Running SQL to Azure - register_virtual_dataset"):
            print("Running SQL to Azure - register_virtual_dataset")
        assert True

    @allure.story("Register Schema")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sql_to_azure
    @pytest.mark.register_schema
    def test_register_schema_sql(self):
        with allure.step("Running SQL to Azure - register_schema"):
            print("Running SQL to Azure - register_schema")
        assert True

    @allure.story("Register Task")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sql_to_azure
    @pytest.mark.register_task
    def test_register_task_sql(self):
        with allure.step("Running SQL to Azure - register_task"):
            print("Running SQL to Azure - register_task")
        assert True

    @allure.story("Register Task Flows")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sql_to_azure
    @pytest.mark.register_task_flows
    def test_register_task_flows_sql(self):
        with allure.step("Running SQL to Azure - register_task_flows"):
            print("Running SQL to Azure - register_task_flows")
        assert True

    @allure.story("Data Reconciliation")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sql_to_azure
    @pytest.mark.data_reconciliation
    def test_data_reconciliation(self):
        with allure.step("Running dataReconciliation"):
            print("Running dataReconciliation")
        assert True
