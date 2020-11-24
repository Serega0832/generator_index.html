from horoscope import generate_prophecies
from datetime import datetime as dt


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Сгенерировали страницу, {name}')  # Press Ctrl+8 to toggle the breakpoint.
# проверка на последние изменения

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
    return '<body>' + body + '</body>'


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
