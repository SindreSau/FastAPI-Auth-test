import asyncio

from fastapi import Security, HTTPException, Depends
from fastapi.security.api_key import APIKeyHeader
from starlette.status import HTTP_403_FORBIDDEN
from config import get_settings

api_key_header = APIKeyHeader(name="API_KEY", auto_error=False)


async def get_api_key(api_key_header: str = Security(api_key_header)):
    settings = get_settings()
    if api_key_header == settings.API_KEY:
        return api_key_header
    else:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Could not validate API KEY")
