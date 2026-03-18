from pydantic import BaseModel

class GenerateRequest(BaseModel):
    topic: str
    user_id: str


class GenerateResponse(BaseModel):
    result: str
    source: str