from fasthtml.common import *
from dataclasses import dataclass
from collections import Counter

app, rt = fast_app()

@dataclass
class Product:
    id: int; name: str; price: float

@dataclass 
class Cart:
    items: Counter = None
    def __post_init__(self): self.items = Counter()
    def add(self, product): 
        self.items[product.id] += 1
    def total(self): 
        return sum(next(p.price for p in products if p.id == pid) * qty for pid, qty in self.items.items())

    def summary(self): 
        return ", ".join(f"{next(p.name for p in products if p.id == pid)} (x{qty})" for pid, qty in self.items.items())

products = [Product(1, "Laptop", 999), Product(2, "Mouse", 29.99), Product(3, "Keyboard", 59.99)]
cart = Cart()

def product_card(p): 
    return Card(
        H3(p.name), 
        P(f"${p.price}"),
        Button(
            "Add to Cart", 
            hx_post=f"/cart/add/{p.id}", 
            hx_target="#cart-summary",  #  บอกให้ HTMX อัปเดตแค่ cart-summary
            hx_swap="innerHTML"  #  แทนที่เฉพาะเนื้อหา ไม่ใช่ปุ่มเอง
        )
    )

@rt('/')
def get():
    return Titled("Shopping Cart",
        Div(*[product_card(p) for p in products], id="product-list"),
        Div(P("Cart is empty"), id="cart-summary"))

@rt('/cart/add/{id}')
def post(id: int):
    product = next(p for p in products if p.id == id)
    cart.add(product)
    return Div(
        H3("Cart Summary:"),
        P(cart.summary()),
        P(f"Total: ${cart.total():.2f}"),
        # hx_swap_oob="innerHTML",
        id="cart-summary"
    )

serve()
