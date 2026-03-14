from pydantic import BaseModel
from typing import List


class CeremonyResponse(BaseModel):
    slug: str
    couple_names: str
    date: str
    livestream_url: str
    stages: List[str]
    current_stage: str
