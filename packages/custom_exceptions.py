from fastapi.responses import JSONResponse
from fastapi import Request


class ObjectDoesNotExist(Exception):
    def __init__(self, detail: str):
        self.detail = detail


# Define a custom exception handler
async def custom_exception_handler(request: Request, exc: ObjectDoesNotExist):
    return JSONResponse(
        content={"error": exc.detail},
        status_code=404,
    )
