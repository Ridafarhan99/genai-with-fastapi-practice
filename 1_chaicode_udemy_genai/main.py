from fastapi import FastAPI

app = FastAPI(
    title="Shop read-only menu API",
    description="Read-only menu API"
)

# decorator
@app.get("/")
def root():
    return {"message": "welcome to read-only menu API"}