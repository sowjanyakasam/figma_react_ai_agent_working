from pathlib import Path
class Validator:
    def validate(self,code:str):
        errors=[]
        if "```" in code: errors.append("Markdown fences found")
        if "export" not in code: errors.append("No export found")
        if "AppButton" not in code: errors.append("Expected AppButton not used")
        return {"success":not errors,"errors":errors}
    def validate_file(self,path:Path):
        return self.validate(path.read_text(encoding="utf-8"))
