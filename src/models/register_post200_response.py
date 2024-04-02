# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class RegisterPost200Response(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    RegisterPost200Response - a model defined in OpenAPI

        api_key: The api_key of this RegisterPost200Response [Optional].
    """

    api_key: Optional[str] = Field(alias="apiKey", default=None)

RegisterPost200Response.update_forward_refs()
