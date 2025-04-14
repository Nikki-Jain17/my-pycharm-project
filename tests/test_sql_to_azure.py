import pytest

@pytest.mark.P1
class TestSQLToAzure:

    @pytest.mark.sql_to_azure
    @pytest.mark.register_physical_dataset
    def test_register_physical_dataset_sql(self):
        print("Running SQL to Azure - register_physical_dataset")
        assert True

    @pytest.mark.sql_to_azure
    @pytest.mark.register_virtual_dataset
    def test_register_virtual_dataset_sql(self):
        print("Running SQL to Azure - register_virtual_dataset")
        assert True

    @pytest.mark.sql_to_azure
    @pytest.mark.register_schema
    def test_register_schema_sql(self):
        print("Running SQL to Azure - register_schema")
        assert True

    @pytest.mark.sql_to_azure
    @pytest.mark.register_task
    def test_register_task_sql(self):
        print("Running SQL to Azure - register_task")
        assert True

    @pytest.mark.sql_to_azure
    @pytest.mark.register_task_flows
    def test_register_task_flows_sql(self):
        print("Running SQL to Azure - register_task_flows")
        assert True

    @pytest.mark.sql_to_azure
    @pytest.mark.data_reconciliation
    def test_data_reconciliation(self):
        print("Running dataReconciliation")
        assert True