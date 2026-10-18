from typing import Any
from .models import DesignIR

class FigmaParser:
    def parse(self,raw:dict[str,Any])->DesignIR:
        if "size" in raw and "style" in raw:
            s=raw["style"]
            return DesignIR(component_type="button",name=raw.get("name","Button"),
                text=raw.get("text",""),width=raw["size"].get("width"),
                height=raw["size"].get("height"),variant=raw.get("variant"),
                background=s.get("background"),text_color=s.get("textColor"),
                border_radius=s.get("borderRadius"),font_size=s.get("fontSize"),
                font_weight=s.get("fontWeight"),padding_x=s.get("paddingX"),
                padding_y=s.get("paddingY"))
        name=raw.get("name","Component")
        if raw.get("type") in {"INSTANCE","COMPONENT"} and "BUTTON" in name.upper():
            return DesignIR(component_type="button",name=name,text=self._text(raw),
                            width=(raw.get("size") or raw.get("absoluteBoundingBox") or {}).get("width"),
                            height=(raw.get("size") or raw.get("absoluteBoundingBox") or {}).get("height"))
        return DesignIR(name=name)

    def _text(self,node):
        if node.get("type")=="TEXT": return node.get("characters","")
        return next((x for c in node.get("children",[]) or [] if (x:=self._text(c))),"")
