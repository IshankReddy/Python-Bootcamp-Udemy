from fastapi import FastAPI
import asyncio

app = FastAPI()

# Asynchronous route that simulates a long-running task
@app.get("/delay/")
async def delay_response():
    await asyncio.sleep(3)
    return {"message": "This took 3 seconds!"}