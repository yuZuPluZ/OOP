from fasthtml.common import *

app, rt = fast_app()

products = [
   {"name": "Laptop", "description": "High performance laptop"},
   {"name": "Mouse", "description": "Wireless mouse"},
   {"name": "Keyboard", "description": "Mechanical keyboard"}
]

def search_products(search: str):
   return [p for p in products if search.lower() in p["name"].lower()]

@rt('/')
def get():
   return Titled("AJAX Demo",
       Form(Input(id="search", placeholder="Search products..."), 
           hx_get="/search", target_id="results", hx_trigger="keyup delay:500ms"),
       Div(id="results"))

@rt('/search')
def get(search: str):
   results = search_products(search)
   return Div(*[Card(H3(p["name"]), P(p["description"])) for p in results])

serve()

