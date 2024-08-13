from fastapi import Depends, FastAPI
from fastapi.security.api_key import APIKey
import auth

app = FastAPI()


@app.get("/")
async def health() -> dict:
    return {"health": "check complete"}


@app.get("/public")
async def public() -> dict:
    return {"public": "data"}


@app.get("/private")
async def private(api_key: APIKey = Depends(auth.get_api_key)) -> dict:
    return {"private": "data"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
