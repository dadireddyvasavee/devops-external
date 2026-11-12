from app import create_app


def test_home_returns_successful_response():
    client = create_app().test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_home_returns_json_content_type():
    client = create_app().test_client()

    response = client.get("/")

    assert response.mimetype == "application/json"


def test_home_returns_default_message(monkeypatch):
    monkeypatch.delenv("MSG", raising=False)
    client = create_app().test_client()

    response = client.get("/")

    assert response.get_json() == {"message": "Hello DevOps!"}


def test_home_uses_message_from_environment(monkeypatch):
    monkeypatch.setenv("MSG", "CI is green")
    client = create_app().test_client()

    response = client.get("/")

    assert response.get_json() == {"message": "CI is green"}


def test_home_uses_explicit_message():
    client = create_app("Custom message").test_client()

    response = client.get("/")

    assert response.get_json() == {"message": "Custom message"}


def test_temporary_failure_for_ci_log_capture():
    assert False, "Intentional temporary failure to capture CI logs"