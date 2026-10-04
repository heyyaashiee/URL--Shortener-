"""
Pydantic schemas define what shape of data the API accepts and returns.
Keeping these separate from the SQLAlchemy models (models.py) is a common
FastAPI pattern -- it lets you control exactly what's exposed over the API.
"""

from datetime import datetime
from pydantic import BaseModel, HttpUrl, ConfigDict


class URLCreateRequest(BaseModel):
    """What the client sends to POST /shorten"""
    original_url: HttpUrl


class URLResponse(BaseModel):
    """What the API sends back after creating a short URL"""
    model_config = ConfigDict(from_attributes=True)  # lets us return ORM objects directly

    short_code: str
    original_url: str
    created_at: datetime
