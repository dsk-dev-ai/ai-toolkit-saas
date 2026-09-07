from pydantic import BaseModel


class GenerateRequest(BaseModel):
    topic: str


class GenerateResponse(BaseModel):
    result: str
    source: str
