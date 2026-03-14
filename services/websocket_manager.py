from fastapi import WebSocket
from typing import Dict, List


class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, List[WebSocket]] = {}

    async def connect(self, slug: str, websocket: WebSocket):
        await websocket.accept()

        if slug not in self.active_connections:
            self.active_connections[slug] = []

        self.active_connections[slug].append(websocket)

    def disconnect(self, slug: str, websocket: WebSocket):
        self.active_connections[slug].remove(websocket)

    async def broadcast(self, slug: str, message: dict):
        if slug in self.active_connections:
            for connection in self.active_connections[slug]:
                await connection.send_json(message)


manager = ConnectionManager()