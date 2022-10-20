from django.urls import path
from django.utils.timezone import now, datetime

from ninja import NinjaAPI, Schema, errors

api = NinjaAPI(title="NBI Ninja")
errors.set_default_exc_handlers(api)


class APIStatusScheme(Schema):
    status: str
    request: datetime


class ServiceUnavailableError(Exception):
    pass


@api.get("/status", response=APIStatusScheme)
async def api_status(request):
    """Returns the status of the API server"""
    return api.create_response(
        request,
        dict(status="ok", request=now()),
        status=200,
    )


@api.exception_handler(ServiceUnavailableError)
def service_unavailable(request, exc):
    return api.create_response(
        request,
        {"message": "Please retry later"},
        status=503,
    )


urlpatterns = [
    path("", api.urls),
]
