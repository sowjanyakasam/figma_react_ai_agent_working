import re, requests
from typing import Any

class SampleFigmaProvider:
    def get_node(self, node_id: str)->dict[str,Any]:
        return {
            "id":node_id,"type":"INSTANCE","name":"Primary Button",
            "size":{"width":120,"height":40},"text":"Submit","variant":"primary",
            "style":{"background":"#2563EB","textColor":"#FFFFFF",
                     "borderRadius":6,"fontSize":14,"fontWeight":600,
                     "paddingX":20,"paddingY":12}
        }

class FigmaRestProvider:
    # Replace this boundary with the company's Figma MCP client later.
    def __init__(self, token:str):
        if not token: raise ValueError("FIGMA_TOKEN is required")
        self.token=token

    @staticmethod
    def parse_url(url:str):
        m=re.search(r"figma\.com/(?:design|file)/([^/]+)",url)
        if not m: raise ValueError("Could not find Figma file key")
        key=m.group(1)
        nm=re.search(r"[?&]node-id=([^&]+)",url)
        return key, nm.group(1).replace("-",
":") if nm else None

    def get_node(self,url:str):
        key,node_id=self.parse_url(url)
        headers={"X-Figma-Token":self.token}
        if node_id:
            r=requests.get(f"https://api.figma.com/v1/files/{key}/nodes",
                           headers=headers,params={"ids":node_id},timeout=30)
            r.raise_for_status()
            return r.json()["nodes"][node_id]["document"]
        r=requests.get(f"https://api.figma.com/v1/files/{key}",headers=headers,timeout=30)
        r.raise_for_status()
        return r.json()["document"]
