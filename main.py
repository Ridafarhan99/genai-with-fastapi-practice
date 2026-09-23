from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
def get_item_by_ids(item_id: int):
    return {"item_id" : item_id}