from fasthtml.common import *

app, rt = fast_app()

products = [] # เก็บข้อมูลสินค้าในรายการ

@rt("/product/{id}")
def delete(id: int):
    # ลบ product ที่มี id ตรงกัน
    products.delete(id)
    return Titled(
        "Product Deleted",
        Div(
            H2("Success!"),
            P(f"Product {id} has been deleted")
        )
    )

