from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Container(
        Card(
            # เนื้อหาหลัก
            H2("สินค้าของเรา"),
            P("รายละเอียดสินค้า"),
            P("ราคา: $99"),
            
            # กำหนดส่วนหัว
            header=H3("สินค้าแนะนำ"),
            
            # กำหนดส่วนท้าย
            footer=Button("ซื้อเลย")
        )
    )

@rt("/profile")
def get():
    return Container(
        Card(
            # เนื้อหาหลัก
            H2("John Doe"),
            P("Web Developer"),
            P("john@email.com"),
            
            # ส่วนหัว
            header=H3("Profile Card"),
            
            # ส่วนท้าย
            footer=Button("Edit Profile")
        )
    )

@rt("/service")
def get():
    return Container(
        H1("Our Services"),
        Grid(
            Card(
                H3("Basic Plan"),
                P("Perfect for starters"),
                P("$10/month"),
                footer=Button("Select")
            ),
            
            Card(
                H3("Pro Plan"),
                P("For professionals"),
                P("$20/month"),
                footer=Button("Select")
            ),

            Card(
                H3("Enterprise"),
                P("For large teams"),
                P("$50/month"),
                footer=Button("Contact Us")
            )
        )
    )

@rt("/grid")
def get():
    return Container(
        H1("Color Grid Example"),
        Grid(
            # ช่องที่ 1 - สีฟ้า
            Div(
                H2("Box 1"),
                P("Content 1"),
                style="background-color: #e6f3ff; padding: 20px;"
            ),
            # ช่องที่ 2 - สีเขียว
            Div(
                H2("Box 2"),
                P("Content 2"),
                style="background-color: #e6ffe6; padding: 20px;"
            ),
            # ช่องที่ 3 - สีชมพู
            Div(
                H2("Box 3"),
                P("Content 3"),
                style="background-color: #ffe6e6; padding: 20px;"
            )
        )
    )

@rt("/h")
def get():
    return Container(
        H1("Our Services"),
        Grid(
            # Card ที่ 1 - พื้นหลังสีฟ้าอ่อน
            Card(
                H3("Basic Plan"),
                P("Perfect for starters"),
                P("$10/month"),
                footer=Button("Select"),
                style="background-color: #e6f3ff;"
            ),
            
            # Card ที่ 2 - พื้นหลังสีเขียวอ่อน
            Card(
                H3("Pro Plan"),
                P("For professionals"),
                P("$20/month"),
                footer=Button("Select"),
                style="background-color: #e6ffe6;"
            )
        )
    )

@rt("/hw")
def get():
    return Container(
        Card(
            H3("Square Card"),
            P("Width and height are equal"),
            style="width: 200px; height: 200px;"
        )
    )

@rt("/hw2")
def get():
    return Container(
        Card(
            H3("Flexible Card"),
            P("Has min and max dimensions"),
            style="min-width: 200px; max-width: 400px; min-height: 100px; max-height: 300px;"
        )
    )

@rt("/size")
def get():
    return Container(
        # ขนาดแบบ pixel (px)
        Card(
            P("Fixed pixel size"),
            style="width: 300px;"
        ),
        
        # ขนาดแบบ percentage (%)
        Card(
            P("Percentage size"),
            style="width: 50%;"
        ),
        
        # ขนาดแบบ viewport width (vw)
        Card(
            P("Viewport width"),
            style="width: 50vw;"
        ),
        
        # ขนาดแบบ rem (สัมพันธ์กับขนาด font ของ root)
        Card(
            P("Size in rem"),
            style="width: 20rem;"
        )
    )

serve()

