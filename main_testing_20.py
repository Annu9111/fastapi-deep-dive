from fastapi.testclient import TestClient
from main20 import app

client = TestClient(app)

#Test Home API
def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message" : "hello annu"}
    
#Test ADD API
def test_add():
    response = client.get("/add?a=5&b=3")
    assert response.status_code ==200
    assert response.json()=={"result":8}
    