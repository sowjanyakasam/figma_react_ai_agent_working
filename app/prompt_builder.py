from .models import DesignIR,ComponentMatch

def build(design:DesignIR,matches:list[ComponentMatch])->str:
    best=matches[0].model_dump_json(indent=2) if matches else "None"
    return f'''You are a senior React + TypeScript UI engineer.

Convert ONE Figma component into production-oriented React code.

DESIGN IR:
{design.model_dump_json(indent=2)}

BEST EXISTING COMPANY COMPONENT:
{best}

RULES:
- Prefer the existing company component.
- Do not invent a duplicate component.
- Return only one complete TSX file.
- No markdown fences.
- No unnecessary business logic.
- Use semantic React/TypeScript.

Return the complete file content.
'''
