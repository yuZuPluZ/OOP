from fasthtml.common import *

app, rt = fast_app()

# กำหนดข้อมูล products
products = [
    ['001', 'Hard Disk', 5000],
    ['002', 'CPU', 7000],
    ['003', 'Main Board', 4000]
]

@rt("/products")
def get():
    return Titled(
        "Products List",
        Table(
            Thead(Tr(Th("ID"), Th("Product Name"), Th("Price"))),
            Tbody(*[Tr(Td(p[0]), Td(p[1]), Td(f"${p[2]:,}")) for p in products])
        )
    )

serve()