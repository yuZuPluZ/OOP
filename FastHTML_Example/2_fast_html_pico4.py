from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Container(
        Card(
            H3("Title1"),
            P("Content"),
            style="text-align: center;"  # left, right, center, justify
        ),

        Card(
            H3("Title2", style="color: red;"),
            P("Content"),
            style="""
                color: red                   
                background-color:rgb(180, 235, 248);    
                border: 2px solid black;  
            """
        ),

        Card(
            H3("Title3"),
            P("Content"),
            style="""
                margin: 10px;           /* ระยะห่างรอบๆ */
                padding: 20px;          /* ระยะห่างขอบ */
                margin-top: 10px;       /* ระยะห่างด้านบน */
                margin-bottom: 10px;    /* ระยะห่างด้านล่าง */
            """
        ),

        Card(
            H3("Title4"),
            style=""" 
            border: 1px solid black;  /* ขนาด สไตล์ สี ขอบ */
            border-radius: 10px;      /* ความโค้งขอบมน */
            border-width: 2px;        /* ความหนาขอบ */
            """
            ),

        Card(
            H3("Title5"),
            style="""
            font-size: 16px;          /* ขนาดตัวอักษร */
            font-weight: bold;        /* ความหนาตัวอักษร */
            font-style: italic;       /* สไตล์ตัวอักษร */
            line-height: 1.5;         /* ระยะห่างระหว่างบรรทัด */
            """
            ),

        Card(
            H3("Title6"),
            style="box-shadow: 2px 2px 5px rgba(0,0,0,0.2);"  # แนวนอน แนวตั้ง การกระจาย สี
            ),

        Card(
            H3("Hover Me"),
            style="""
                transition: all 0.3s;
                cursor: pointer;
            """,
            hx_on="mouseenter: this.style.backgroundColor = '#f0f0f0';\
            mouseleave: this.style.backgroundColor = '';"
        ),

        Card(
            H3("Title7"),
            style="""
            display: flex;           /* block, inline, flex, grid */
            visibility: visible;     /* hidden, collapse */
            opacity: 0.5;            /* ความโปร่งใส (0.0 - 1.0) */
            """
            ),

        Card(
            H3("Title8"),
            style="""
            position: relative;      /* static, relative, absolute, fixed */
            top: 10px;               /* ระยะห่างจากด้านบน */
            left: 20px;              /* ระยะห่างจากด้านซ้าย */
            z-index: 1;              /* ลำดับการซ้อนทับ */
            """
            ),
    
        Card(
            H2("Important Card"),
            P("This is highlighted content"),
            style="""
                background-color: #f8f9fa;
                padding: 20px;
                margin: 10px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                text-align: center;
                color: #333;
            """
        ),
        
        Card(
            H2("Feature Card"),
            P("Special feature description"),
            style="""
                background-color: #e3f2fd;
                padding: 15px;
                margin: 15px;
                border: 2px solid #2196f3;
                border-radius: 10px;
                font-size: 16px;
                line-height: 1.6;
            """
        )
    )



serve()

