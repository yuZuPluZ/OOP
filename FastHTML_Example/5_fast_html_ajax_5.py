from fasthtml.common import *
from datetime import datetime

app, rt = fast_app()

@rt('/')
def get():
    return Titled("FastHTML Demo",
        Form(
            Input(
                name="query",
                placeholder="พิมพ์เพื่อค้นหา...",
                hx_get="/search",
                hx_trigger="keyup delay:500ms",
                hx_target="#search-results"
            ),
            Div(id="search-results")  # ส่วนแสดงผลลัพธ์การค้นหา
        ),
        Div(
            id="update-section",
            hx_get="/updates",
            hx_trigger="every 3s"
        )
    )

@rt('/search')
def get(req):
    query = req.query_params.get("query", "").strip()
    
    if query:
        results = [f"ผลลัพธ์ที่เกี่ยวข้องกับ '{query}'", "ตัวอย่างผลลัพธ์ 1", "ตัวอย่างผลลัพธ์ 2"]
        return Div(*[P(result) for result in results])
    else:
        return P("กรุณาป้อนคำค้นหา")

@rt('/updates')
def get():
    return P(f"อัปเดตล่าสุด: {datetime.now().strftime('%H:%M:%S')}")

serve()
