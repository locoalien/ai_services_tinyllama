'''
##################### TinyLlama + FastAPI + Docker #########################################
Autor: Santiago Gonzalez Acevedo 
Twitter: @locoalien
github: https://github.com/locoalien/ai_services_tinyllama
Python 3.11+
'''
import logging
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from starlette.requests import Request

log = logging.getLogger(__name__)

startup_msg_fmt = """
 Starting up API Services
"""

async def on_http_error(request: Request, exc: HTTPException):
    return JSONResponse({'detail': exc.detail}, status_code=exc.status_code)

async def on_startup(app):
    log.info("INICIO APP AI")

def startup_event_handler(app):
    async def start_app() -> None:
        await on_startup(app)

    return start_app