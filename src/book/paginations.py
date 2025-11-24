from fastapi_pagination import Params

class CustomParams(Params):
    size: int = 2 