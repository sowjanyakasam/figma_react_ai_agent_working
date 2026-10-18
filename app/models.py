from typing import Literal
from pydantic import BaseModel, Field

class DesignIR(BaseModel):
    component_type: Literal["button","unknown"]="unknown"
    name: str
    text: str=""
    width: float|None=None
    height: float|None=None
    variant: str|None=None
    background: str|None=None
    text_color: str|None=None
    border_radius: float|None=None
    font_size: float|None=None
    font_weight: int|None=None
    padding_x: float|None=None
    padding_y: float|None=None

class ComponentMatch(BaseModel):
    component_name: str
    import_path: str
    props: list[str]=Field(default_factory=list)
    confidence: float
