from horoscope import generate_prophecies
from datetime import datetime as dt


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Сгенерировали страницу, {name}')  # Press Ctrl+8 to toggle the breakpoint.


def generate_head(title):
    head = f'''<head>
<meta charset=utf-8>
<link rel='stylesheet' type='text/css' href='css/bootstrap.min.css'/>
<title>{title}</title>
</head>'''
    return head


def generate_body(header, paragraphs):
    body = '<h1>' + header + '</h1>'
    for p in paragraphs:
        body += f'<p>{p}</p>'
    template ='''
    <div class="d-flex flex-column flex-md-row align-items-center p-3 px-md-4 mb-3 bg-white border-bottom shadow-sm">
  <h5 class="my-0 mr-md-auto font-weight-normal">Company name</h5>
  <nav class="my-2 my-md-0 mr-md-3">
    <a class="p-2 text-dark" href="#">Features</a>
    <a class="p-2 text-dark" href="#">Enterprise</a>
    <a class="p-2 text-dark" href="#">Support</a>
    <a class="p-2 text-dark" href="#">Pricing</a>
  </nav>
  <a class="btn btn-outline-primary" href="#">Sign up</a>
</div>
    '''
    return '<body>' + template+ body + '</body>'


def generate_page(head, body):
    page = f'<html>{head}{body}</html>'
    return page


def save_page(title, header, paragraphs, output='index.html'):
    fp = open(output, 'w')
    page = generate_page(
        head = generate_head(title),
        body = generate_body(header = header, paragraphs = paragraphs)
    )
    print(page, file=fp)
    fp.close()


today = dt.now().date()
save_page(
    title = 'Гороскоп на сегодня',
    header = f'Что на {today} говорит',
    paragraphs = generate_prophecies(),
)


if __name__ == '__main__':
    print_hi('Джулиан')
