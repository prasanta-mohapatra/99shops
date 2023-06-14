from fastapi import APIRouter

app = APIRouter()


@app.get("/")
async def get_all_shops():
    pass


@app.post("/")
async def create_shop():
    # Your logic for creating a shop goes here
    pass


@app.get("/{shop_id}")
async def get_shop(shop_id: int):
    # Your logic for retrieving a specific shop goes here
    pass


@app.put("/{shop_id}")
async def update_shop(shop_id: int):
    # Your logic for updating a specific shop goes here
    pass


@app.delete("/{shop_id}")
async def delete_shop(shop_id: int):
    # Your logic for deleting a specific shop goes here
    pass
