from fasthtml.common import *

app, rt = fast_app(
       hdrs=(
        Style("""
            .highlight { color: red; font-weight: bold; }
            .important { background-color: yellow; padding: 2px; }
            .box { border: 2px solid black; padding: 10px; margin-top: 10px; background-color: #f0f0f0; }
        """),
    )
)

@rt('/')
def get():
    return Titled(
        "FastHTML Example",
        Div(
            P("นี่คือย่อหน้า"),
            A("ไปที่เว็บไซต์", href="https://example.com"),
            Img(src="https://example.com/image.jpg", alt="ตัวอย่างภาพ"),
            Table(
                Tr(
                    Th("หัวข้อ 1"),
                    Th("หัวข้อ 2")
                ),
                Tr(
                    Td(Span("ข้อมูล 1", cls="highlight")),  
                    Td("ข้อมูล 2")
                ),
                Tr(
                    Td("ข้อมูล 3"),
                    Td(Span("ข้อมูล 4 (สำคัญ)", cls="important")),  
            ),
            Div(P("เนื้อหาใน Div"), cls="box")
            )
        )
    )

serve()

