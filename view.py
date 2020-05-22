from starlette.responses import JSONResponse
from starlette.routing import Route
from models import User

async def homepage(request):
    rv = await User.create(nickname="begyy")
    return JSONResponse(rv.to_dict())

routes = [
    Route("/", endpoint=homepage)
]
