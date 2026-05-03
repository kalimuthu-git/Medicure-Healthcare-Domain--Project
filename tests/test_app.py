import pytest
import json
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test home page returns 200"""
    response = client.get('/')
    assert response.status_code == 200

def test_health_check(client):
    """Test health endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'healthy'
    assert data['service'] == 'Medicure Healthcare'

def test_get_doctors(client):
    """Test doctors API returns list"""
    response = client.get('/doctors')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert len(data) > 0
    assert 'name' in data[0]
    assert 'specialty' in data[0]

def test_get_departments(client):
    """Test departments API returns list"""
    response = client.get('/departments')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert len(data) > 0

def test_contact_form(client):
    """Test contact form submission"""
    payload = {'name': 'John', 'email': 'john@test.com', 'message': 'Test message'}
    response = client.post(
        '/contact',
        data=json.dumps(payload),
        content_type='application/json'
    )
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'success'

def test_404_not_found(client):
    """Test 404 for invalid routes"""
    response = client.get('/nonexistent-page')
    assert response.status_code == 404
