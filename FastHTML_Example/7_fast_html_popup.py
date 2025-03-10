from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Titled("Pop-up Demo",
        Button("Show Pop-up", hx_get="/popup", hx_target="body", hx_swap="beforeend"),
        Style("""
            .popup {
                position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                background: rgba(0, 0, 0, 0.5); display: flex;
                align-items: center; justify-content: center; z-index: 1000;
            }
            .popup-content {
                background: white; padding: 20px; border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.25);
                min-width: 300px; text-align: center;
            }
            .popup button {
                margin-top: 10px; padding: 5px 10px; border: none; background: #ff5b5b;
                color: white; border-radius: 5px; cursor: pointer;
            }
            .popup button:hover {
                background: #ff2b2b;
            }
        """)
    )

@rt("/popup")
def get_popup():
    return Div(
        Div(
            H2("Hello!"),
            P("This is a simple pop-up window."),
            Button("Close", onclick="document.getElementById('popup').remove()"),
            cls="popup-content"
        ),
        id="popup", cls="popup"
    )

serve()

