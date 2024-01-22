'''
##################### TinyLlama + FastAPI + Docker #########################################
Autor: Santiago Gonzalez Acevedo 
Twitter: @locoalien
github: https://github.com/locoalien/ai_services_tinyllama
Python 3.11+
'''
from api_v1.routes import tinyllama
from fastapi import APIRouter

router = APIRouter()

router.include_router(tinyllama.router) 

