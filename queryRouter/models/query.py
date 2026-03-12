from pydantic import BaseModel
from typing import Optional

class ParsedQuery(BaseModel):
    command: str  # Changed from keyword
    query: str    # Changed from payload

class Shortcut(BaseModel):
    keyword: str
    url: str
    search: Optional[str] = None

class PortSettings(BaseModel):
    port: int