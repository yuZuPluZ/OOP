from fasthtml.common import *
from dataclasses import dataclass

app, rt = fast_app()

@dataclass
class Product:
   id: int; name: str; price: float

@dataclass 
class Cart:
   items: list = None
   def __post_init__(self): self.items = []
   def add(self, product): self.items.append(product)
   def total(self): return sum(item.price for item in self.items)

products = [Product(1, "Laptop", 999), Product(2, "Mouse", 29.99), 
            Product(3, "Keyboard", 59.99)]
cart = Cart()

def product_card(p): return Card(H3(p.name), P(f"${p.price}"), 
   Button("Add to Cart", hx_post=f"/cart/add/{p.id}", target_id="product-list"))

@rt('/')
def get():
   return Titled("Shopping Cart",
       Div(*[product_card(p) for p in products], id="product-list"),
       Div(f"Cart Total: ${cart.total():.2f}", id="cart-summary"))

@rt('/cart/add/{id}')
def post(id: int):
   cart.add([p for p in products if p.id == id][0])
   return (Div(*[product_card(p) for p in products]),
           Div(f"Cart Total: ${cart.total():.2f}", 
           hx_swap_oob="innerHTML", id="cart-summary"))

serve()


