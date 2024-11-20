from fastapi import FastAPI

# Create FastAPI app instance
app = FastAPI()

# Define a basic route
@app.get("/")
def read_root():
    return {"message": "Hello World"}
