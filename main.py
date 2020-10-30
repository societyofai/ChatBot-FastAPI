from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = FastAPI()

templates = Jinja2Templates(directory="templates")

english_bot = ChatBot("Chatterbot")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/getChatBotResponse")
def get_bot_response(msg: str):
    return str(english_bot.get_response(msg))

if __name__ == "__main__":
    uvicorn.run("main:app")