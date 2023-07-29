from typing import Dict, Union, Type, List, Any, Optional

from fastapi import APIRouter
from fastapi.params import Depends
from pydantic import BaseModel
from starlette.responses import Response


class TypedAPIRouter(BaseModel):
    """ Typed APIRouter. Needed for initializer """

    router: APIRouter
    prefix: str = str()
    tags: List[str] = []
    dependencies: List[Depends] = []
    responses: Dict[Union[int, str], Dict[str, Any]] = dict()
    default_response_class: Optional[Type[Response]] = None

    class Config:

        arbitrary_types_allowed = True
