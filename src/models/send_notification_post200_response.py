# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class SendNotificationPost200Response(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SendNotificationPost200Response - a model defined in OpenAPI

        success: The success of this SendNotificationPost200Response [Optional].
        message_id: The message_id of this SendNotificationPost200Response [Optional].
    """

    success: Optional[bool] = Field(alias="success", default=None)
    message_id: Optional[str] = Field(alias="messageId", default=None)

SendNotificationPost200Response.update_forward_refs()