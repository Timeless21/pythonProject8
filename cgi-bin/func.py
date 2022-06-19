import statistics


def func1(x: list):
    return statistics.mean(x)


def func2(x: list):
    v = []
    for i in x:
        if i < 0:
            v.append(i)
    v.sort()
    total = v[-1]
    return total


def func3(x: list):
    return sorted(x, key=abs)


def htmlprint(l, ch, f1, f2, f3):
    print("Content-type: text/html; charset=utf-8\n")
    print("""<!DOCTYPE HTML>
            <html>
                <head>
                    <meta charset = " utf-8, cp1251">
                    <title>Данные анализа</title>
                </head>
                <body>
                    <h1>Вывод данных формы!</h1>""")
    print("         <p>Ваш логин: {}</p>".format(l))
    print("         <p>Числовая последовательность {}</p>".format(ch))
    print("         <p>Результат 1 группы: {}</p>".format(f1))
    print("         <p>Результат 2 группы: {}</p>".format(f2))
    print("         <p>Результат 3 группы: {}</p>".format(f3))
    print("""   </body>
            </html>""")


def htmlprlog(x):
    print("Content-type: text/html; charset=utf-8\n")
    print("""<!DOCTYPE HTML>
            <html>
                <head>

                </head>
                <body>
                    <h1>РЕЗУЛЬТАТЫ</h1>""")
    print("         <p>Ваше имя: {}</p>".format(x))
    print("         <p>Дополнительные функции не были выбраны</p>")
    print("""   </body>
            </html>""")
