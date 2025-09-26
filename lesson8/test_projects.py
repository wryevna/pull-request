
import pytest
from yougile_api import YougileAPI


class TestProjects:

    def test_create_project_positive(self):
        data = {"title": "Project Positive"}
        response = YougileAPI.create_project(data)
        assert response.status_code == 201
        body = response.json()
        assert "id" in body

    def test_create_project_negative_no_name(self):
        data = {}
        response = YougileAPI.create_project(data)
        assert response.status_code == 400

    @pytest.fixture
    def new_project(self):
        data = {"title": "Temp Project"}
        response = YougileAPI.create_project(data)
        assert response.status_code == 201
        body = response.json()
        return body

    def test_update_project_positive(self, new_project):
        project_id = new_project["id"]
        response = YougileAPI.update_project(
            project_id,
            {"title": "Updated Title"},
        )
        assert response.status_code == 200

    def test_update_project_negative_invalid_id(self):
        response = YougileAPI.update_project(
            "invalid_id",
            {"title": "Bad Update"},
        )
        assert response.status_code in [400, 404]

    def test_get_project_positive(self, new_project):
        project_id = new_project["id"]
        response = YougileAPI.get_project(project_id)
        assert response.status_code == 200
        body = response.json()
        assert body["id"] == project_id

    def test_get_project_negative_invalid_id(self):
        response = YougileAPI.get_project("invalid_id")
        assert response.status_code in [400, 404]
