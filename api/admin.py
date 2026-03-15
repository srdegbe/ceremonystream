from fastapi import APIRouter, HTTPException
from services.websocket_manager import manager
from api.ceremonies import dummy_ceremony
from schemas.admin import StageUpdateRequest

router = APIRouter()


@router.post("/ceremony/{slug}/stage")
async def update_stage(slug: str, request: StageUpdateRequest):
    stage = request.stage

    # Validate ceremony slug
    if slug != dummy_ceremony["slug"]:
        raise HTTPException(status_code=404, detail="Ceremony not found")

    # Validate stage
    if stage not in dummy_ceremony["stages"]:
        raise HTTPException(status_code=400, detail="Invalid stage")

    # Update current stage
    dummy_ceremony["current_stage"] = stage

    # Broadcast to all connected clients
    await manager.broadcast(slug, {"type": "stage_update", "stage": stage})

    return {"status": "success", "current_stage": stage}
