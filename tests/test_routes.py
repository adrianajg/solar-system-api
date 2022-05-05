def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == "No planets found with that name."

def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id":1,
        "name":"Mercury",
        "description":"Mercury's description",
        "gravity":2
    }

def test_get_one_planet_no_data(client):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body["details"] == "No planet with id 1 found"

def test_get_all_planets_with_valid_records(client, two_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [
    {
        "description": "Mercury's description",
        "gravity": 2,
        "id": 1,
        "name": "Mercury"
    },
    {
        "description": "A riveting description of Venus.",
        "gravity": 3.1,
        "id": 2,
        "name": "Venus"
    }
    ]

def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "description": "Mercury's description",
        "gravity": 2,
        "id": 1,
        "name": "Mercury"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == "Planet Mercury successfully created"
    