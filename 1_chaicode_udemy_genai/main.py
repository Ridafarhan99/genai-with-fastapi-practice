from fastapi import FastAPI, Query, HTTPException
from models import MenuItem, MenuResponse
from data import menu_items

app = FastAPI(title="Shop read-only menu API", description="Read-only menu API")


# decorator
@app.get("/")
def root():
    return {"message": "welcome to read-only menu API"}


# /menu
# /menu?category=chai


# dependency injection
@app.get("/menu", response_model=MenuResponse)
def get_menu(category: str | None = Query(None, description="get all menu Query desc")):
    if category:
        filtered = [item for item in menu_items if item["category"] == category.lower()]
        if not filtered:
            raise HTTPException(status_code=404, detail="No item found in category")
        return MenuResponse(count=len(filtered), items=filtered)

    return MenuResponse(count=len(menu_items), items=menu_items)


@app.get("/menu/{id}", response_model=MenuItem)
def get_item(id: int):
    for item in menu_items:
        if item["id"] == id:
            return item
    raise HTTPException(status_code=404, detail=f"Menu Item with {id} not found")
