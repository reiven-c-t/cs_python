#28-1-2018
C:\Users\pc - user\Anaconda3\python.exe
"C:\Program Files\JetBrains\PyCharm Community Edition 2017.2.4\helpers\pydev\pydevconsole.py"
65514
65515
Python
3.6
.1 | Anaconda
4.4
.0(64 - bit) | (default, May
11
2017, 13: 25:24) [MSC v.1900 64 bit(AMD64)]
Type
"copyright", "credits" or "license"
for more information.
    IPython
    5.3
    .0 - - An
    enhanced
    Interactive
    Python.
?         -> Introduction and overview
of
IPython
's features.
% quickref -> Quick
reference.
help      -> Python
's own help system.
object?   -> Details
about
'object', use
'object??'
for extra details.
    PyDev
    console: using
    IPython
    5.3
    .0
import sys;

print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['C:\\Users\\pc-user\\PycharmProjects\\cs_python', 'C:/Users/pc-user/PycharmProjects/cs_python'])
Python
3.6
.1 | Anaconda
4.4
.0(64 - bit) | (default, May
11
2017, 13: 25:24) [MSC v.1900 64 bit(AMD64)]
on
win32
flag = True
flag = False
for i in range(10):
    print(i)

0
1
2
3
4
5
6
7
8
9
for i in range(10):
    for j in range(5):
        if i == 5 and j == 3:
            flag = True
    if flag:
        break
