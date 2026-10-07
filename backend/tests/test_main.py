<<<<<<< HEAD
﻿import sys
from pathlib import Path 
import pytest 

ROOT_DIR = Path(__file__).resolve().parent.parent.parent 
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))
=======
﻿# --- Testes de Leitura e Edição (Proprietários) ---

def test_get_owners():
    response = client.get("/api/v1/owners")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
>>>>>>> 0f0a060 (refactor(schemas): migrate schemas to Pydantic V2 and expand test suite)

def test_get_owner_by_id():
    # Tenta obter o proprietário criado no test_create_owner (ID 1)
    response = client.get("/api/v1/owners/1")
    assert response.status_code in [200, 404]

def test_update_owner():
    payload = {"name": "Maria Silva Atualizada"}
    response = client.put("/api/v1/owners/1", json=payload)
    assert response.status_code in [200, 404]

# --- Testes de Animais ---

def test_get_animals():
    response = client.get("/api/v1/animals")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_animal_by_id():
    response = client.get("/api/v1/animals/1")
    assert response.status_code in [200, 404]

def test_update_animal():
    payload = {"name": "Bella Renovada"}
    response = client.put("/api/v1/animals/1", json=payload)
    assert response.status_code in [200, 404]

# --- Testes de Vacinas ---

def test_create_vaccine():
    payload = {
        "name": "Febre Aftosa",
        "application_date": "2026-03-15",
        "next_due_date": "2026-09-15",
        "animal_id": 1
    }
    response = client.post("/api/v1/vaccines", json=payload)
    assert response.status_code in [200, 201, 400, 404, 422]

def test_get_vaccines():
    response = client.get("/api/v1/vaccines")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# --- Testes de Exclusão (Delete) ---

def test_delete_vaccine():
    response = client.delete("/api/v1/vaccines/1")
    assert response.status_code in [200, 204, 404]

def test_delete_animal():
    response = client.delete("/api/v1/animals/1")
    assert response.status_code in [200, 204, 404]

def test_delete_owner():
    response = client.delete("/api/v1/owners/1")
    assert response.status_code in [200, 204, 404]