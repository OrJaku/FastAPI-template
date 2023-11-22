import logging
from typing import Dict, Any

from fastapi import APIRouter
from sqlalchemy.orm import Session

from configuration import conf, get_user_conf


router = APIRouter(
    tags=['Base'],
    prefix='/api',
    responses={404: {"description": "Not found"}}
)


@router.get("/")
def main():
    """
    Base application endpoint
    
    """
    return {"message": f"App"}

