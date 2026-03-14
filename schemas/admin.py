from pydantic import BaseModel

class StageUpdateRequest(BaseModel):
    stage: str