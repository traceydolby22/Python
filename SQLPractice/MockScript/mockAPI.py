import requests

def test_donor_endpoint():
    response = requests.post("https://api.example.com/donors", json={"name": "Test Donor", "amount": 50})
    assert response.status_code == 200 # means request succeeded
    data = response.json()
    assert "donor_id" in data
    assert data["ammount"] == 50