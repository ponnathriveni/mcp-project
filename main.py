from fastapi import FastAPI
from agent import research

main = FastAPI()

@app.get("/")
def home():
    return {"message": "Autonomous Research Agent"}

@app.post("/research")
def research_api(topic: str):

    result = research(topic)

    return {
        "topic": topic,
        "report": result
    }
