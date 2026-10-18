from app.parser import FigmaParser

def test_button():
    raw={"type":"INSTANCE","name":"Primary Button","size":{"width":120,"height":40},
         "text":"Submit","variant":"primary","style":{"background":"#2563EB","textColor":"#fff",
         "borderRadius":6,"fontSize":14,"fontWeight":600,"paddingX":20,"paddingY":12}}
    ir=FigmaParser().parse(raw)
    assert ir.component_type=="button"
    assert ir.text=="Submit"
    assert ir.width==120
