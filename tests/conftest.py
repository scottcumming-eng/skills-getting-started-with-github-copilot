import copy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


BASE_ACTIVITIES = copy.deepcopy(app_module.activities)


@pytest.fixture
def client():
    return TestClient(app_module.app)


@pytest.fixture
def reset_activities():
    def _reset():
        app_module.activities.clear()
        app_module.activities.update(copy.deepcopy(BASE_ACTIVITIES))

    return _reset
