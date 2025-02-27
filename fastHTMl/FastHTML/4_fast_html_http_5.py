from fasthtml.common import *
from dataclasses import dataclass

app, rt = fast_app()
products = [] # เก็บข้อมูลสินค้าในรายการ

@dataclass
class Product:
   name: str; price: float; description: str

@rt("/product/{id}")
def put(id: int, product: Product):
    # อัพเดตข้อมูล product ที่มี id ตรงกัน
    updated = products.update(product, id)
    return Titled(
        "Product Updated",
        Div(
            H2("Success!"),
            P(f"Updated product: {updated.name}")
        )
    )

