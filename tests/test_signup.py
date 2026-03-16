import src.app as app_module


def test_signup_success_adds_participant(client, reset_activities):
    reset_activities()
    email = "newstudent@mergington.edu"

    response = client.post(f"/activities/Chess%20Club/signup?email={email}")

    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {email} for Chess Club"
    assert email in app_module.activities["Chess Club"]["participants"]


def test_signup_fails_when_activity_not_found(client, reset_activities):
    reset_activities()

    response = client.post("/activities/NotARealActivity/signup?email=test@mergington.edu")

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_fails_for_duplicate_participant(client, reset_activities):
    reset_activities()

    response = client.post("/activities/Chess%20Club/signup?email=michael@mergington.edu")

    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up"


def test_signup_fails_when_activity_is_full(client, reset_activities):
    reset_activities()
    participants = app_module.activities["Chess Club"]["participants"]
    app_module.activities["Chess Club"]["max_participants"] = len(participants)

    response = client.post("/activities/Chess%20Club/signup?email=fullcase@mergington.edu")

    assert response.status_code == 400
    assert response.json()["detail"] == "Activity is full"
