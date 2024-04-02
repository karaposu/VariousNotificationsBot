# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class RegisterPostRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    RegisterPostRequest - a model defined in OpenAPI

        username: The username of this RegisterPostRequest.
        email: The email of this RegisterPostRequest.
    """

    username: str = Field(alias="username")
    email: str = Field(alias="email")

RegisterPostRequest.update_forward_refs()