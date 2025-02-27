from fasthtml.common import *
from dataclasses import dataclass

app, rt = fast_app()
products = [] # เก็บข้อมูลสินค้าในรายการ

@dataclass
class Product:
   name: str; price: float; description: str

@rt("/")
def get():
   return Titled("Product Management",
       Form(Input(id="name",name="name",placeholder="Name"), 
            Input(id="price",name="price",type="number",step="0.01"), 
            Input(id="description",name="description",placeholder="Description"), 
            Button("Add"),method="post",action="/product"),
       Table(Thead(Tr(Th("Name"), Th("Price"), Th("Description"))),
             Tbody(*[Tr(Td(p.name), Td(f"${p.price:,.2f}"), Td(p.description)) 
                     for p in products])))

@rt("/product")
def post(product: Product):
   products.append(product)
   return RedirectResponse("/", status_code=303)

serve()


