import os

import pytest

os.environ.setdefault("API_KEY", "test-key")
os.environ.setdefault("APP_NAME", "Test API")
os.environ.setdefault("ENVIRONMENT", "test")
os.environ.setdefault("DEBUG", "false")

from fastapi.testclient import TestClient

from git_day_practice.api import app


@pytest.fixture(scope="session")
def client() -> TestClient:

    return TestClient(app)
