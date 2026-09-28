from fastapi import FastAPI

app = FastAPI(
    title="Pincode lookup API",
    description="Autofill city and state from indian pincode during checkout",
)


@app.get("/")
def root():
    return {"message": "Pincode API"}
