from fastapi.testclient import TestClient
from httpx import ASGITransport, AsyncClient
import pytest


from main import app, MyPerson

sync_client = TestClient(app)

# @pytest.mark.anyio
# async def test_backend_used() -> None:
#     '''
#     This was meant to determine async library used.
#     It was always trying to use `trio`. Have just let it have `trio`
#     '''
#     import sniffio
#     backend = sniffio.current_async_library()
#     print(f"\n>>> Detected backend: {backend}")
#     assert backend == "asyncio"

@pytest.mark.anyio
async def test_read_root() -> None:
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.get("/")

    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_ping() -> None:
    response = sync_client.get("/ping")
    assert response.status_code == 200
    assert response.text == '"pong"'

@pytest.mark.anyio
async def test_get_person() -> None:
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        response = await ac.get("/person/jack")

    assert response.status_code == 200
    assert response.json() == MyPerson(name="jack", age=20).model_dump()
