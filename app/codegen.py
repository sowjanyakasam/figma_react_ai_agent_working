from pathlib import Path
from .models import DesignIR,ComponentMatch
from .prompt_builder import build
from .llm import LLMGenerator

TEMPLATE='''import React from "react";
import {{ AppButton }} from "@company/ui";

export type PrimaryButtonProps = {{
  children?: React.ReactNode;
  disabled?: boolean;
  loading?: boolean;
}};

export function PrimaryButton({{
  children = "{text}",
  disabled = false,
  loading = false,
}}: PrimaryButtonProps) {{
  return (
    <AppButton variant="primary" disabled={{disabled}} loading={{loading}}>
      {{children}}
    </AppButton>
  );
}}
'''

class CodeGenerator:
    def __init__(self,use_llm=False):
        self.use_llm=use_llm
        self.llm=LLMGenerator() if use_llm else None
    def generate(self,design:DesignIR,matches:list[ComponentMatch]):
        return self.llm.generate(build(design,matches)) if self.use_llm else TEMPLATE.format(text=design.text or "Submit")
    def write(self,code,root:Path):
        p=root/"src"/"components"/"PrimaryButton.tsx"
        p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(code,encoding="utf-8")
        return p
