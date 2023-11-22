import logging
from typing import Dict, Any

from fastapi import APIRouter
from fastapi_utils.tasks import repeat_every
from sqlalchemy.orm import Session

from configuration import conf, get_user_conf


router = APIRouter(
    tags=['Base'],
    prefix='/api',
    responses={404: {"description": "Not found"}}
)

@router.on_event("startup")
def application_start_repeat() -> None:
    logging.info("App is running..")


@router.get("/")
def main():
    """
    Base application endpoint
    
    """
    return {"message": f"App"}

