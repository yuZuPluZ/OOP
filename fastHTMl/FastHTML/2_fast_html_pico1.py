from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Container(  # <- Container จะถูกจัดรูปแบบด้วย PicoCSS
        H1("Welcome"),  # <- H1 จะได้สไตล์จาก PicoCSS
        P("This is a paragraph"),  # <- P จะได้สไตล์จาก PicoCSS
        Button("Click me")  # <- Button จะได้สไตล์จาก PicoCSS
    )

serve()



