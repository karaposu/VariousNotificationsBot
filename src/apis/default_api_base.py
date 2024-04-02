# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from models.register_post200_response import RegisterPost200Response
from models.register_post_request import RegisterPostRequest
from models.send_notification_post200_response import SendNotificationPost200Response
from models.send_notification_post_request import SendNotificationPostRequest
from security_api import get_token_ApiKeyAuth

from impl.services.send_notification import SendNotificationService

class BaseDefaultApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseDefaultApi.subclasses = BaseDefaultApi.subclasses + (cls,)
    def register_post(
        self,
        register_post_request: RegisterPostRequest,
    ) -> RegisterPost200Response:
        """Registers a new user and returns a unique API key for authentication."""
        ...


    def send_notification_post(
        self,
        send_notification_post_request: SendNotificationPostRequest,
    ) :
        """Sends a notification message to the user&#39;s Telegram account."""

        sn=SendNotificationService(send_notification_post_request)

