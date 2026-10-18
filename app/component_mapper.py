from .models import DesignIR,ComponentMatch

CATALOG=[
 {"name":"AppButton","import_path":"@company/ui",
  "props":["variant","size","disabled","loading"],"keywords":["button","primary","secondary"]},
 {"name":"PlainButton","import_path":"@company/ui",
  "props":["disabled"],"keywords":["button"]},
]

class ComponentMapper:
    def find(self,design:DesignIR):
        out=[]
        for x in CATALOG:
            score=0.0
            if design.component_type in x["keywords"]: score+=.5
            if design.variant and design.variant in x["keywords"]: score+=.4
            if design.component_type=="button" and x["name"]=="AppButton": score+=.1
            if score:
                out.append(ComponentMatch(component_name=x["name"],import_path=x["import_path"],
                    props=x["props"],confidence=min(score,.99)))
        return sorted(out,key=lambda x:x.confidence,reverse=True)
