from fasthtml.common import *

page = Html(
    Head(Title('Some page')),
    Body(Div('Some text, ', A('A link', href='https://example.com'), \
        Img(src="https://placehold.co/200"), cls='myclass')))
print(to_xml(page))

