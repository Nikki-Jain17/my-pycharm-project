def pytest_addoption(parser):
    parser.addoption(
        "--flow", action="store", default=None, help="Specify which flow to run"
    )
    parser.addoption(
        "--component", action="store", default=None, help="Specify which component to run"
    )
