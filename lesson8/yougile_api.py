
import requests

BASE_URL = "https://yougile.com/api-v2"
# Нужно будет вписать токен
TOKEN = (
    "токен"
)

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
}


class YougileAPI:

    @staticmethod
    def create_project(data):
        return requests.post(
            f"{BASE_URL}/projects",
            headers=HEADERS,
            json=data,
        )

    @staticmethod
    def update_project(project_id, data):
        return requests.put(
            f"{BASE_URL}/projects/{project_id}",
            headers=HEADERS,
            json=data,
        )

    @staticmethod
    def get_project(project_id):
        return requests.get(
            f"{BASE_URL}/projects/{project_id}",
            headers=HEADERS,
        )
