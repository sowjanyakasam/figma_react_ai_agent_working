# Figma → React AI Agent

Runnable prototype: Figma provider/MCP boundary → parser → Design IR → component mapper → LLM → React code → validation.

## Run
1. Python 3.11+
2. `python -m venv .venv`
3. Windows: `\.venv\Scripts\Activate.ps1`
4. `pip install -r requirements.txt`
5. Copy `.env.example` to `.env`

No API key required:
`python -m app.main --sample`

With LLM:
`python -m app.main --sample --llm`

Real Figma REST bridge:
`python -m app.main --figma-url "YOUR_FIGMA_URL"`

Set `FIGMA_TOKEN` in `.env`.

The Figma REST provider is deliberately isolated. Replace it later with your company's approved Figma MCP client without changing the parser, Design IR, mapper, generator, or validator.

Generated code is written only under `generated/`.
