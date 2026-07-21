import time

# Contrato del recurso post: campo -> tipo esperado
CONTRATO_USER = {
    "id": int,
    "name": str,
    "username": str,
    "email": str,
}

# BASE_URL = "https://jsonplaceholder.typicode.com"

def test_listar_users(api):
    # respuesta = httpx.get(f"{BASE_URL}/users")
    respuesta = api.get("/users")
    assert respuesta.status_code == 200
    assert len(respuesta.json()) == 10

def cumple_contrato(recurso: dict, contrato: dict) -> bool:
    """Valida presencia y tipo de cada campo (el JSON Schema de la S3, versión KISS)."""
    return all(
        campo in recurso and isinstance(recurso[campo], tipo)
        for campo, tipo in contrato.items()
    )

def test_detalle_cumple_contrato(api):
    respuesta = api.get("/users/1")

    assert respuesta.status_code == 200
    assert cumple_contrato(respuesta.json(), CONTRATO_USER)

def test_crear_user(api):
    name = f"Nelson {time.time_ns()}"
    payload = {
        "name": name,
        "username": "nelson",
        "email": "nelson@test.com",
    }

    respuesta = api.post("/users", json=payload)

    assert respuesta.status_code == 201
    creado = respuesta.json()
    assert isinstance(creado["id"], int)
    assert creado["name"] == name

def test_actualizar_user(api):
    payload = {
        "id": 1,
        "name": "Nombre actualizado!",
        "username": "nuevo_usuario",
        "email": "nuevo@test.com",
    }
    respuesta = api.put("/users/1", json=payload)

    assert respuesta.status_code == 200
    # assert respuesta.json()["name"] == payload["name"]

    actualizado = respuesta.json()
    assert actualizado["name"] == payload["name"]
    assert actualizado["username"] == payload["username"]
    assert actualizado["email"] == payload["email"]

def test_eliminar_user(api):
    respuesta = api.delete("/users/1")
    assert respuesta.status_code == 200
    assert respuesta.json() == {}