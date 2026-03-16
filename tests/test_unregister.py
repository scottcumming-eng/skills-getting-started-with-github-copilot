import src.app as app_module


def test_unregister_success_removes_participant(client, reset_activities):
    reset_activities()
    email = "michael@mergington.edu"

    response = client.request("DELETE", f"/activities/Chess%20Club/unregister?email={email}")

    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from Chess Club"
    assert email not in app_module.activities["Chess Club"]["participants"]


def test_unregister_fails_when_activity_not_found(client, reset_activities):
    reset_activities()

    response = client.request("DELETE", "/activities/NotARealActivity/unregister?email=test@mergington.edu")

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_fails_for_non_registered_student(client, reset_activities):
    reset_activities()

    response = client.request("DELETE", "/activities/Chess%20Club/unregister?email=absent@mergington.edu")

    assert response.status_code == 404
    assert response.json()["detail"] == "Student not registered for this activity"
