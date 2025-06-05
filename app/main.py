from fastapi import FastAPI, Request
from app.crews.crew_manager import kickoff_crew

app = FastAPI()

@app.post("/kickoff/")
async def kickoff_crew_endpoint(request: Request):
    data = await request.json()
    result = kickoff_crew(data)
    return {"result": result}
