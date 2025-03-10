from fasthtml.common import *

app, rt = fast_app()

@rt('/')
def get():
    return Div(
        # แสดงจำนวนสินค้าในตะกร้า
        Div("สินค้าในตะกร้า: 0", id="cart-count"),
        
        # รายการสินค้า
        Card(
            "สินค้า A ",
            Button("เพิ่มลงตะกร้า",
                hx_post="/add-to-cart", hx_target="#message"  # เป้าหมายหลัก
            )
        ),
        # พื้นที่แสดงข้อความ
        Div(id="message")
    )

@rt('/add-to-cart')
def post():
    # ตอบกลับด้วยหลาย element
    # 1. ข้อความหลักไปที่ #message (เป้าหมายหลัก)
    # 2. อัพเดทจำนวนในตะกร้าไปที่ #cart-count (OOB Swap)
    return (
        "เพิ่มสินค้าลงตะกร้าแล้ว",  # ไปที่ #message
        Div("สินค้าในตะกร้า: 1", id="cart-count", 
            hx_swap_oob="true"  # บอกว่านี่คือ OOB Swap
        )
    )

serve()