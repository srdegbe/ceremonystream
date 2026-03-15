from pydantic import BaseModel
from typing import List


class Ceremony(BaseModel):
    slug: str
    couple_names: str
    date: str
    livestream_url: str
    stages: List[str]
    current_stage: str


# Example stages we will use:

# Opening Prayer
# Family Introduction
# Knocking
# Drinks Presentation
# Acceptance
# Blessings
