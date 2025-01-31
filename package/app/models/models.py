from pydantic import BaseModel
from typing import List

class Route(BaseModel):
    origin: str
    destination: str
    routes: List[str]  # Define 'routes' as a list of strings
