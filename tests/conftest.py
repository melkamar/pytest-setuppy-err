import pytest
import logging

def pytest_addoption(parser):
    parser.addoption('--config', default='conf.ini', help='Path to the testing config file.')


@pytest.fixture
def configfile(request):
    return request.config.getoption("--config")


@pytest.fixture(scope='session', autouse=True)
def init_config(configfile):
    print(f'Init config: {configfile}')
