
import cgi
import sys
import codecs
import random
from func import *

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

form = cgi.FieldStorage()
name = form.getfirst('name', '')
fc1 = form.getfirst('fc1', '')
fc2 = form.getfirst('fc2', '')
fc3 = form.getfirst('fc3', '')

list_func = [fc1, fc2, fc3]

m = [random.randint(-25, 40) for i in range(22)]

if fc1 == 'on':
    result1 = func1(m)
else:
    result1 = 'Не выбран'

if fc2 == 'on':
    result2 = func2(m)
else:
    result2 = 'Не выбран'

if fc3 == 'on':
    result3 = func3(m)
else:
    result3 = 'Не выбран'

if 'on' not in list_func:
    htmlprlog(name)
else:
    htmlprint(name, m, result1, result2, result3)
