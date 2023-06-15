import pytest
from starlette import status
from starlette.testclient import TestClient

shop_base_url = "/shop"


@pytest.fixture
async def create_shop() -> dict:
    return {
        "id": 1,
        "name": "Shop A",
        "latitude": 40.7128,
        "longitude": -74.006,
        "address": "1st Avenue",
        "city": "New York",
        "state": "New York",
        "country": "United States",
        "postal_code": "10001",
    }


@pytest.mark.anyio
async def test_create_shop(client: TestClient, create_shop):
    r = client.post(
        f"{shop_base_url}/",
        json=create_shop,
    )
    assert r.status_code == status.HTTP_201_CREATED


@pytest.mark.anyio
async def test_create_shop_conflict(client: TestClient, create_shop):
    r = client.post(
        f"{shop_base_url}/",
        json=create_shop,
    )
    assert r.status_code == status.HTTP_409_CONFLICT


@pytest.mark.anyio
async def test_get_all_shops_filter(client: TestClient):
    r = client.get(f"{shop_base_url}?location='1st Avenue'&perimeter=20")
    assert r.status_code == status.HTTP_200_OK


@pytest.mark.anyio
async def test_get_all_shops(client: TestClient):
    r = client.get(f"{shop_base_url}/")
    assert r.status_code == status.HTTP_200_OK


@pytest.mark.anyio
async def test_get_shop(client: TestClient):
    r = client.get(f"{shop_base_url}/1")
    assert r.status_code == status.HTTP_200_OK


@pytest.mark.anyio
async def test_get_shop_negative(client: TestClient):
    r = client.get(f"{shop_base_url}/2")
    assert r.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.anyio
async def test_update_shop(client: TestClient):
    r = client.patch(
        f"{shop_base_url}/1",
        json={
            "name": "Shop Share",
            "postal_code": "10002",
        },
    )
    assert r.status_code == status.HTTP_200_OK


@pytest.mark.anyio
async def test_update_shop_negative(client: TestClient):
    r = client.patch(
        f"{shop_base_url}/2",
        json={
            "name": "Shop Share",
            "postal_code": "10002",
        },
    )
    assert r.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.anyio
async def test_delete_shop(client: TestClient):
    r = client.delete(f"{shop_base_url}/1")
    assert r.status_code == status.HTTP_200_OK


@pytest.mark.anyio
async def test_delete_shop_negative(client: TestClient):
    r = client.delete(f"{shop_base_url}/2")
    assert r.status_code == status.HTTP_404_NOT_FOUND
