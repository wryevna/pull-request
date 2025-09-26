
import pytest
from yougile_api import YougileAPI


@pytest.fixture
def new_project():
    data = {"name": "Test Project"}
    response = YougileAPI.create_project(data)
    project = response.json()
    yield project
