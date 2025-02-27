from fasthtml.common import *

app, rt = fast_app()


@rt("/")
def get():
    return (Titled(
    "Create event",
    Container(
    H1("Our Website"),

        # Container ย่อยที่ 1 - ชิดซ้าย
        Container(
            H2("Section 1"),
            P("Content for section 1"),
            Button("Learn More"),
            style="text-align: left; background-color: #f0f0f0;"
        ),

        # Container ย่อยที่ 2 - ชิดขวา
        Container(
            H2("Section 2"),
            P("Content for section 2"),
            Button("Read More"),
            style="text-align: right; background-color: #e0e0e0;"
            )
        )
    )
    )


serve()