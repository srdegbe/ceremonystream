from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from services.websocket_manager import manager

router = APIRouter()


@router.websocket("/ws/ceremony/{slug}")
async def websocket_endpoint(websocket: WebSocket, slug: str):

    await manager.connect(slug, websocket)

    try:
        while True:
            data = await websocket.receive_json()

            # Validate type
            if "type" not in data:
                continue

            if data["type"] == "chat":
                # Example: {"type": "chat", "name": "Ama", "message": "Congrats!"}
                await manager.broadcast(slug, data)

            elif data["type"] == "stage_update":
                # Example: {"type": "stage_update", "stage": "Knocking"}
                await manager.broadcast(slug, data)

    except WebSocketDisconnect:
        manager.disconnect(slug, websocket)