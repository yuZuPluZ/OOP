from fasthtml.common import *

app, rt = fast_app()

@rt('/')
def get():
    return Titled("FastHTML Demo",
        Form(
            Input(id="title", placeholder="Enter text"),
            Button("Add"),
            hx_post="/add",
            hx_target="#items",
            hx_swap="beforeend"
        ),
        Div(id="items")  # Container for dynamic items
    )

@rt('/add')
def post(title: str):
    # สร้าง unique id สำหรับแต่ละ card
    card_id = f"card-{hash(title)}"
    return Card(
        title,
        Button("Delete",
            hx_delete=f"/remove/{card_id}",  # ส่ง id ไปกับ request
            hx_target=f"#{card_id}",         # ระบุเป้าหมายด้วย id
            hx_swap="outerHTML"
        ),
        id=card_id  # กำหนด id ให้กับ Card
    )

@rt('/remove/{card_id}')  # รับ parameter card_id จาก URL
def delete(card_id: str):
    return ""

serve()

