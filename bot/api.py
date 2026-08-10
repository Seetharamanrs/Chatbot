from fastapi import FastAPI
from pydantic import BaseModel
from bot.app_1 import generate_answer
app=FastAPI()


class Inputquestion(BaseModel):
    data:str

@app.route("/question")
def question(data:Inputquestion):
    response=generate_answer(data)
    return response.output_text
