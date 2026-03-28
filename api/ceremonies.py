from fastapi import APIRouter
from schemas.ceremony import CeremonyResponse

router = APIRouter()

dummy_ceremony = {
    "slug": "ella-michael",
    "couple_names": "Ella ❤️ Michael",
    "date": "2026-03-28",
    "livestream_url": "https://www.youtube.com/watch?v=c9Z4oN8DSQ8",
    "stages": [
        "Opening Prayer",
        "Greetings by groom's family",
        "Welcome by bride's family",
        "Knocking",
        "Family Introduction",
        "Drinks Presentation",
        "Acceptance",
        "Blessings",
    ],
    "current_stage": "Opening Prayer",
}


@router.get("/ceremony/{slug}", response_model=CeremonyResponse)
def get_ceremony(slug: str):
    if slug == dummy_ceremony["slug"]:
        return dummy_ceremony
    return {"error": "Ceremony not found"}
