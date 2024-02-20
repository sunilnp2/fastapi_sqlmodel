from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi import FastAPI, Request
from routers import users, blogs
from packages.custom_exceptions import ObjectDoesNotExist, custom_exception_handler
from fastapi_pagination import add_pagination

app = FastAPI()


add_pagination(app)


# middleware section-----------------------------------------------

# app.add_middleware(HTTPSRedirectMiddleware)

# @app.middleware("http")
# async def add_process_time_header(request: Request, call_next):
#     start_time = time.time()
#     response = await call_next(request)
#     process_time = time.time() - start_time
#     response.headers["X-Process-Time"] = str(process_time)
#     return response


# @app.middleware("http")
# async def middleware_one(request: Request, call_next):
#     print("Executing middleware_one before route handler")
#     response = await call_next(request)
#     print("Executing middleware_one after route handler")
#     return response
#
#
# @app.middleware("http")
# async def middleware_two(request: Request, call_next):
#     print("Executing middleware_two before route handler")
#     response = await call_next(request)
#     print("Executing middleware_two after route handler")
#     return response


# app.add_middleware(TrustedHostMiddleware, allowed_hosts=["127.0.0.1", "localhost"])

# exception Handler section ----------------------------
app.add_exception_handler(ObjectDoesNotExist, custom_exception_handler)

# adding router
app.include_router(users.router, tags=["User"])
app.include_router(blogs.router, tags=["Blog"])
