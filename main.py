from fastapi import FastAPI
from controllers import calculadora_controller

app = FastAPI()
app.include_router(calculadora_controller.router)
