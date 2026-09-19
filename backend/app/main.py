from fastapi import FastAPI

app = FastAPI(
    title="NextGen Bank - FastAPI Backend",
    description="Fully feature banking app built with fastAPI"
)

@app.get("/")
def home():
    return {"message": "Welcome to the nextgen bank API"}