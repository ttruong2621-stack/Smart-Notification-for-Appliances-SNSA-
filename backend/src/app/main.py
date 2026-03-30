from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class EventMessage(BaseModel):
    """Event message model"""

    deviceID: str
    event: str
    soundName: str
    timestampt: str


@app.post("/event")
async def eventTrigger(event_message: EventMessage):
    return {"message": "Hello World"}
