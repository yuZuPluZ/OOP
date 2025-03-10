from fasthtml.common import *
from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    username: str
    pwd: str

@dataclass
class Book:
    id: int
    title: str
    auther: str
    price: int
    pages: int
    published: bool
    published_date: str

    def __ft__(self):
        """สร้าง FastHTML component สำหรับแสดงข้อมูลหนังสือในตาราง"""
        show = AX(self.title, f'/books/{self.id}', id_curr)
        edit = AX('edit', f'/edit/{self.id}', id_curr)
        dt = '✅ ' if self.title else ''
        return Tr(
            Td(dt, show), Td(self.auther), Td(self.price), Td(self.pages),
            Td(self.published), Td(self.published_date), Td(edit),
            id=f'book-{self.id}'
        )

class Library:
    
    def __init__(self):
        self._books = []  # รายการหนังสือทั้งหมด
        self._users = {}  # dictionary เก็บข้อมูลผู้ใช้
        self._next_book_id = 1  # ตัวนับสำหรับสร้าง ID หนังสือ

    def add_user(self, username: str, password: str) -> User:
        if username not in self._users:
            self._users[username] = User(username=username, pwd=password)
        return self._users[username]

    def verify_user(self, username: str, password: str) -> bool:
        user = self._users.get(username)
        return user and user.pwd == password

    def add_book(self, book: Book) -> Book:
        book.id = self._next_book_id
        self._next_book_id += 1
        self._books.append(book)
        return book

    def get_book(self, book_id: int) -> Book:
        return next((book for book in self._books if book.id == book_id), None)

    def update_book(self, updated_book: Book) -> Book:
        for i, book in enumerate(self._books):
            if book.id == updated_book.id:
                self._books[i] = updated_book
                return updated_book
        return None

    def delete_book(self, book_id: int) -> None:
        self._books = [book for book in self._books if book.id != book_id]

    def get_all_books(self) -> list:
        return self._books

    def filter_books(self, query: str = None, published_only: bool = False) -> list:
        filtered = self._books
        if query:
            query = query.lower()
            filtered = [book for book in filtered 
                       if query in book.title.lower() or 
                          query in book.auther.lower()]
        if published_only:
            filtered = [book for book in filtered if book.published]

        return filtered

# สร้าง instance ของ Library สำหรับใช้งาน
library = Library()

# ฟังก์ชันสำหรับ authentication
def lookup_user(username, password):
    return library.verify_user(username, password)

auth_middleware = user_pwd_auth(lookup_user)

# FastHTML app setup
app = FastHTML(middleware=[auth_middleware],
               hdrs=(picolink,
                     Style(':root { --pico-font-size: 100%; }')))

route = app.route

id_curr = 'current-book'
def mk_input(**kw): return Input(**kw)
def clr_details(): return Div(hx_swap_oob='innerHTML', id=id_curr)
def tid(id): return f'book-{id}'

PER_PAGE = 5

@route("/")
async def get(request, auth):
    page = int(request.query_params.get('page', 1))
    
    all_books = library.get_all_books()
    total_books = len(all_books)
    total_pages = (total_books + PER_PAGE - 1) // PER_PAGE
    
    start = (page - 1) * PER_PAGE
    end = start + PER_PAGE
    paginated_books = all_books[start:end]

    search_bar = Input(
        id="q",
        placeholder="Search by title or author...",
        hx_get="/filter_books",
        target_id='book-rows')

    published_filter = CheckboxX(
        id="published_filter",
        label='Published Only',
        hx_get="/filter_books",
        target_id='book-rows',
        style="margin-bottom: 10px;"
    )

    prev_page = page - 1 if page > 1 else None
    next_page = page + 1 if page < total_pages else None

    pagination = Div(
        A("Previous", href=f"/?page={prev_page}",
          style="margin-right: 10px;") if prev_page else '',
        A("Next", href=f"/?page={next_page}") if next_page else '',
        style="margin-top: 10px; text-align: center;"
    )

    add = Div(
        H4("Add Book"),
        Form(Group(
            mk_input(placeholder="Title", name="title",
                     id="title", required=True),
            mk_input(placeholder="Auther", name="auther", id="auther"),
            mk_input(placeholder="Price", type="number",
                     name="price", id="price"),
            mk_input(placeholder="Pages", type="number",
                     name="pages", id="pages"),
            mk_input(placeholder="Published Date", type="date",
                     name="published_date", id="published_date"),
            Button("Add")),
            CheckboxX(id="published", name="published", label='Published'),
            hx_post="/", target_id='book-rows', hx_swap="beforeend"
        )
    )

    card = Card(H4(f"Books (total {total_books} books)"),
                search_bar,
                published_filter,
                Table(
                    Thead(Tr(Th("Title"), Th("Auther"), Th("Price"), Th("Pages"), 
                           Th("Published"), Th("Published Date"), Th("Edit"))),
                    Tbody(*[book.__ft__()
                          for book in paginated_books], id='book-rows')
                ),
                header=add,
                footer=Div(pagination,
                          Div(id=id_curr))
    )

    top = Grid(Div(A('logout', href=basic_logout(request)),
               style='text-align: right'))

    return Titled(f"Book Management (Page {page})", top, card)

@route("/filter_books")
async def filter_books(request):
    q = request.query_params.get('q', None)
    published_filter = request.query_params.get('published_filter', None)
    page = int(request.query_params.get('page', 1))
    
    filtered_books = library.filter_books(q, published_filter)
    total_books = len(filtered_books)
    total_pages = (total_books + PER_PAGE - 1) // PER_PAGE
    start = (page - 1) * PER_PAGE
    end = start + PER_PAGE
    paginated_books = filtered_books[start:end]

    if not paginated_books:
        return Tr(Td(
            "No books found", colspan=6,
            style="text-align: center; color: red;"))
            
    return Tr(
        *[book.__ft__() for book in paginated_books],
        id='book-rows'
    )

@route("/books/{id}")
async def delete(id: int):
    """Delete a book"""
    library.delete_book(id)
    return clr_details()

@route("/")
async def post(book: Book):
    """Add a new book"""
    new_book = library.add_book(book)
    return new_book, mk_input(hx_swap_oob='true')

@route("/edit/{id}")
async def get(id: int):
    book = library.get_book(id)
    if not book:
        raise NotFoundError()
        
    res = Div(
        H4("Edit Book"),
        Form(Group(Input(id="title"),
                   Input(id="auther"),
                   Input(id="price", type="number"),
                   Input(id="pages", type="number"),
                   Input(id="published_date", type="date"),
                   Button("Save")),
             Hidden(id="id"), CheckboxX(id="published", label='Published'),
             hx_put="/", target_id=tid(id), id="edit")
    )
    return fill_form(res, book)

@route("/")
async def put(book: Book):
    """Update an existing book"""
    updated_book = library.update_book(book)
    return updated_book, clr_details()

@route("/books/{id}")
async def get(id: int):
    book = library.get_book(id)
    if not book:
        raise NotFoundError()
        
    btn = Button('Delete Book', hx_delete=f'/books/{book.id}',
                 target_id=tid(book.id), hx_swap="outerHTML")
    btn.style = 'background-color: red; border: none;'
    return Div(H2(f"Book Title: {book.title}"),
               H6(f"Published: {"Yes" if book.published else "No"}"),
               btn)

# สร้างผู้ใช้ 2 คน
library.add_user("teacher1", "pass1234")  # ผู้ใช้คนที่ 1
library.add_user("teacher2", "pass5678")  # ผู้ใช้คนที่ 2

# เพิ่มข้อมูลตัวอย่างสำหรับทดสอบ
library.add_book(Book(id=0, title="The Great Gatsby", 
                     auther="F. Scott Fitzgerald",
                     price=15, pages=180, published=True, 
                     published_date="1925-04-10"))
library.add_book(Book(id=0, title="1984", 
                     auther="George Orwell",
                     price=12, pages=328, published=True, 
                     published_date="1949-06-08"))
library.add_book(Book(id=0, title="To Kill a Mockingbird", 
                     auther="Harper Lee",
                     price=14, pages=281, published=True, 
                     published_date="1960-07-11"))

library.add_book(Book(id=0, title="The Lord of the Rings", 
                     auther="J.R.R. Tolkien",
                     price=25, pages=1178, published=True, 
                     published_date="1954-07-29"))

library.add_book(Book(id=0, title="Pride and Prejudice", 
                     auther="Jane Austen",
                     price=12, pages=432, published=True, 
                     published_date="1813-01-28"))

library.add_book(Book(id=0, title="The Catcher in the Rye", 
                     auther="J.D. Salinger",
                     price=13, pages=234, published=True, 
                     published_date="1951-07-16"))

library.add_book(Book(id=0, title="Harry Potter and the Philosopher's Stone", 
                     auther="J.K. Rowling",
                     price=18, pages=223, published=True, 
                     published_date="1997-06-26"))

library.add_book(Book(id=0, title="The Da Vinci Code", 
                     auther="Dan Brown",
                     price=16, pages=454, published=True, 
                     published_date="2003-03-18"))

library.add_book(Book(id=0, title="The Alchemist", 
                     auther="Paulo Coelho",
                     price=15, pages=197, published=True, 
                     published_date="1988-01-01"))

library.add_book(Book(id=0, title="One Hundred Years of Solitude", 
                     auther="Gabriel García Márquez",
                     price=17, pages=417, published=True, 
                     published_date="1967-05-30"))

library.add_book(Book(id=0, title="The Little Prince", 
                     auther="Antoine de Saint-Exupéry",
                     price=11, pages=96, published=True, 
                     published_date="1943-04-06"))

library.add_book(Book(id=0, title="Don Quixote", 
                     auther="Miguel de Cervantes",
                     price=20, pages=863, published=True, 
                     published_date="1605-01-16"))

serve()