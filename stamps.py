
pagesList = [{'name': "MainPage", 'action': '/cgi-bin/mainPage.py', 'title': 'Главная страница'},
             {'name': "Rating", 'action': '/cgi-bin/rating.py', 'title': 'Рейтинг'},
             {'name': "SinglePayment", 'action': '/cgi-bin/singlePayment.py', 'title': 'Одиночное начисление злат'},
             {'name': "MultiPayment", 'action': '/cgi-bin/multiPayment.py', 'title': 'Множественное начисление злат'}]


def print_head(header):
    print("Content-type: text/html\n")
    print("""<!DOCTYPE HTML>
            <html>
            <head>
                <meta charset="utf-8">
                <title>""", header, """</title>
                <link rel="stylesheet" href="/shirovlasiki.css">
            </head>
            <body>
    """, sep="")


def print_page_header():
    print("""
        <header>
        <form class="navbar">
          """)
    for page in pagesList:
        print('<button class="navbtn" formaction="', page['action'], '">', page['title'], '</div>')
    print("""
        </div>
        </header>
          """)