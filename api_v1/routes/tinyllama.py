'''
##################### TinyLlama + FastAPI + Docker #########################################
Autor: Santiago Gonzalez Acevedo 
Twitter: @locoalien
github: https://github.com/locoalien/ai_services_tinyllama
Python 3.11+
'''
import logging
from typing import Dict, List
import api_v1.logic.tinyllama as TinyLlamaChat
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from decouple import config
import json

log = logging.getLogger(__name__)

router = APIRouter(prefix="/ai/chatbot", tags=["ChatBot"])

class TinyLlamaRequest(BaseModel):
    prompt: str

class EngineResponse(BaseModel):
    data: List[Dict] = Field(..., description="All available models.")

@router.post('/tinyllama', tags=["ChatBot"],
             summary="ChatBot (TinyLlama).",
             description="Tiny Llama Agente ChatBot.",
             response_class=JSONResponse,
             response_model=EngineResponse)
async def tiny_llama(TinyLlamaRequest: TinyLlamaRequest):
    """Runs a health check on this instance of the API."""
    tinyLlamaResult = TinyLlamaChat.TinyLlamaLogic(TinyLlamaRequest.prompt)
    tiniyLlama_json = tinyLlamaResult.model_query()
    json_results = json.loads(tiniyLlama_json)

    return JSONResponse(json_results, headers={'Access-Control-Allow-Origin': '*'})
