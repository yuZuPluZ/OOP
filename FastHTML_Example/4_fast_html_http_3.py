from fasthtml.common import *

app, rt = fast_app()

@dataclass
class Product:
    name: str
    price: float
    description: str

@rt("/product")
def post(product: Product):
    # FastHTML จะแปลง form data เป็น Product object ให้อัตโนมัติ
    new_product = Product.insert(product)
    return Titled(
        "Product Created",
        Div(
            H2("Success!"),
            P(f"Created product: {new_product.name}")
        )
    )

serve()