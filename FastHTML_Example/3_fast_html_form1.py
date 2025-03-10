from fasthtml.common import *

app, rt = fast_app()

@rt("/")
def get():
    return Container(
        H1("Contact Form"),
        Form(
            Label("Name:", Input(type="text", id="name", placeholder="Enter your name")),
            Label("Email:", Input(type="email", id="email", placeholder="Enter your email")),
            Label("Message:", Textarea(id="message", rows=5, placeholder="Your message")),
            
            Button("Submit", type="submit"),
            method="post",
            action="/submit"
        )
    )

@rt("/submit")
def post(name: str, email: str, message: str):
    return f"ได้รับข้อมูล: {name}, {email}, {message}"

@rt("/registration")
def get():
    return Container(
        H1("Registration Form"),
        Form(
            # Text input
            Label("Username:", 
                Input(type="text", id="username", required=True)),
            
            # Password input
            Label("Password:", 
                Input(type="password", id="password", required=True)),
            
            # Email input
            Label("Email:", 
                Input(type="email", id="email", required=True)),
            
            # Number input
            Label("Age:", 
                Input(type="number", id="age", min="18", max="100")),
            
            # Checkbox
            Label(
                CheckboxX(id="agree", label="I agree to terms", required=True)
            ),
            
            # Radio buttons
            Label("Gender:"),
            Div(
                Label(Input(type="radio", name="gender", value="male"), "Male"),
                Label(Input(type="radio", name="gender", value="female"), "Female"),
                Label(Input(type="radio", name="gender", value="other"), "Other")
            ),
            
            # Select dropdown
            Label("Country:",
                Select(
                    Option("USA", value="usa"),
                    Option("UK", value="uk"),
                    Option("Thailand", value="th"),
                    id="country"
                )
            ),
            
            Button("Register", type="submit"),
            method="post",
            action="/register"
        )
    )

@rt("/profile")
def get():
    return Container(
        H1("Profile Form"),
        Form(
            # กลุ่มข้อมูลส่วนตัว
            Group(
                H3("Personal Information"),
                Label("First Name:", Input(type="text", id="firstname")),
                Label("Last Name:", Input(type="text", id="lastname")),
                Label("Birth Date:", Input(type="date", id="birthdate"))
            ),
            
            # กลุ่มข้อมูลติดต่อ
            Group(
                H3("Contact Information"),
                Label("Email:", Input(type="email", id="email")),
                Label("Phone:", Input(type="tel", id="phone")),
                Label("Address:", Textarea(id="address", rows=3))
            ),
            
            Button("Save Profile", type="submit"),
            method="post",
            action="/save-profile"
        )
    )

@rt("/contact")
def get():
    return Container(
        H1("Contact Us", style="text-align: center;"),
        Form(
            Group(
                Label("Name:", 
                    Input(
                        type="text", 
                        id="name",
                        required=True,
                        pattern="[A-Za-z ]{2,}",  # ต้องเป็นตัวอักษรเท่านั้น
                        title="Name must contain only letters",
                        style="width: 100%;"
                    )
                ),
                
                Label("Email:", 
                    Input(
                        type="email", 
                        id="email",
                        required=True,
                        style="width: 100%;"
                    )
                ),
                
                Label("Subject:", 
                    Input(
                        type="text", 
                        id="subject",
                        required=True,
                        style="width: 100%;"
                    )
                ),
                
                Label("Message:", 
                    Textarea(
                        id="message",
                        rows=5,
                        required=True,
                        style="""
                            width: 100%;
                            resize: vertical;
                        """
                    )
                ),
                
                style="max-width: 500px; margin: 0 auto;"
            ),
            
            Button(
                "Send Message", 
                type="submit",
                style="""
                    width: 100%;
                    margin-top: 20px;
                    background-color: #4CAF50; 
                    color: white;
                """
            ),
            
            method="post",
            action="/send-message",
            style="padding: 20px;"
        )
    )

serve()

