import argparse,json
from pathlib import Path
from .config import FIGMA_TOKEN
from .figma_provider import SampleFigmaProvider,FigmaRestProvider
from .parser import FigmaParser
from .component_mapper import ComponentMapper
from .codegen import CodeGenerator
from .validator import Validator

ROOT=Path(__file__).resolve().parents[1]
GENERATED=ROOT/"generated"

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--sample",action="store_true")
    p.add_argument("--figma-url")
    p.add_argument("--llm",action="store_true")
    a=p.parse_args()
    if not a.sample and not a.figma_url: p.error("Use --sample or --figma-url")
    provider=SampleFigmaProvider() if a.sample else FigmaRestProvider(FIGMA_TOKEN)
    raw=provider.get_node("1:2" if a.sample else a.figma_url)
    design=FigmaParser().parse(raw)
    matches=ComponentMapper().find(design)
    code=CodeGenerator(a.llm).generate(design,matches)
    path=CodeGenerator(False).write(code,GENERATED)
    result=Validator().validate_file(path)
    print("\n=== DESIGN IR ===")
    print(json.dumps(design.model_dump(),indent=2))
    print("\n=== COMPONENT MATCHES ===")
    for m in matches: print(f"- {m.component_name}: {m.confidence:.2f}")
    print("\n=== GENERATED ===\n",path)
    print("\n=== VALIDATION ===\n",json.dumps(result,indent=2))
    if not result["success"]: raise SystemExit(2)

if __name__=="__main__": main()
