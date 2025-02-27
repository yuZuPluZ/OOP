from starlette.testclient import TestClient
from fasthtml.common import *

app = FastHTML()

@app.get("/")
def home():
    return Title("Page Demo"), Div(H1('Hello, World'), P('Some text'), P('Some more text'))

client = TestClient(app)
print(client.get("/").text)