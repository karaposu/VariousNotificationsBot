# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from apis.default_api_base import BaseDefaultApi
import impl
from impl.services.send_notification import SendNotificationService

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from models.extra_models import TokenModel  # noqa: F401
from models.register_post200_response import RegisterPost200Response
from models.register_post_request import RegisterPostRequest
from models.send_notification_post200_response import SendNotificationPost200Response
from models.send_notification_post_request import SendNotificationPostRequest
from security_api import get_token_ApiKeyAuth

router = APIRouter()

ns_pkg = impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)

@router.post(
    "/sendNotification",
    responses={
        200: {"model": SendNotificationPost200Response, "description": "Notification sent successfully"},
    },
    tags=["default"],
    summary="Send a notification",
    response_model_by_alias=True,
)


async def send_notification_post(
    send_notification_post_request: SendNotificationPostRequest = Body(None, description=""),
    token_ApiKeyAuth: TokenModel = Security(
        get_token_ApiKeyAuth
    ),
) :

    service_instance = await SendNotificationService.create(send_notification_post_request)

