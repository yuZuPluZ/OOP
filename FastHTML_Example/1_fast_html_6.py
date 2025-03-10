from fasthtml.common import *

app, rt = fast_app()

@rt('/')
def get():
    return Titled(
        "Lists in FastHTML",
        Div(
            H2("Unordered List"),
            Ul(
                Li("Apple"),
                Li("Banana"),
                Li("Cherry"),
            ),
            H2("Ordered List"),
            Ol(
                Li("Step 1: Prepare ingredients"),
                Li("Step 2: Mix them together"),
                Li("Step 3: Bake in the oven"),
            ),
        )
    )

serve()






