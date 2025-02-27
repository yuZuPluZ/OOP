from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Main(
        H1("This is heading 1"),
        P("This is some text."),
        Hr(),
        H2("This is heading 2"),
        P("This is some other text."),
        Hr(),
        H2("This is heading 2"),
        P("This is some other text.")
    )

serve()