from fastapi import FastAPI
from agent import research

main = FastAPI()

@main.get("/")
def home():
    return {"message": "Autonomous Research Agent"}

@main.post("/research")
def research_api(topic: str):

    result = research(topic)

    return {
        "topic": topic,
        "report": result
    }
