from fasthtml.common import *

app, rt = fast_app()

from fasthtml.common import *

app, rt = fast_app()

@rt("/products")  
def get():    # จะรับ HTTP GET request
    return Titled("Products List", P("List of products"))

@rt("/products")
def post():   # จะรับ HTTP POST request 
    return Titled("Product Created", P("New product added"))

