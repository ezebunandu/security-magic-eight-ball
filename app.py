from fastapi import FastAPI
import random
from mangum import Mangum

app = FastAPI()

magic_eight_ball_strings = [
    "Pizza for everyone",
    "Distract with cats",
    "Don't trust logs",
    "Take deep breath",
    "Do nothing",
    "We are going to need the lawyers for this one",
    "Restart device",
    "Press release time",
    "Buy more coffee",
    "It was the intern",
]


@app.get("/")
def hello_world():
    return {"message": "Hello World"}


@app.get("/magic/{name}")
def magic_eight_ball(name: str):
    string = random.choice(magic_eight_ball_strings)
    return {
        "message": f"hello {name}, the magic eight ball's sage security advice for you is ...'{string}'"
    }


handler = Mangum(app, lifespan="off")
