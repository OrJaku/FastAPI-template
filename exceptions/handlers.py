from exceptions import exceptions
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi import FastAPI

def app_handler(app: FastAPI) -> None:
    @app.exception_handler(exceptions.SomeException)
    async def some_exception_handler(request: Request, exc: exceptions.SomeException) -> JSONResponse:
        status_code = 404
        return JSONResponse(
            status_code=status_code,
            content={
                "status": status_code,
                "message": exc.msg
                },
        )