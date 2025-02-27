from fasthtml.common import *

app, rt = fast_app()

@rt('/')
def get():
    return Form(
        Input(id="title", placeholder="ชื่อบทความ"),
        Textarea(id="content", placeholder="เนื้อหา"),
        Button("บันทึก",
            hx_post="/save",
            hx_target="#result"
        ),
        Div(id="result")
    )

@rt('/save')
def post(title: str, content: str):
    if len(title) < 5:
        return RedirectResponse(url=f"/error-page?msg=ชื่อบทความสั้นเกินไป", status_code=303)
    if len(content) < 10:
        return RedirectResponse(url=f"/error-page?msg=เนื้อหาน้อยเกินไป", status_code=303)
    return "บันทึกสำเร็จ"

@rt('/error-page')
def get(req):
    error_message = req.query_params.get("msg", "เกิดข้อผิดพลาด")  # อ่านค่าจาก URL
    return Div(
        H2("⚠️ เกิดข้อผิดพลาด"),
        P(error_message, style="color: red;")
    )

serve()