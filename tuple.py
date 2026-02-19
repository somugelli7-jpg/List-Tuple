Python 3.15.0a5 (v3.15.0a5:d51cc01c197, Jan 14 2026, 10:47:57) [Clang 17.0.0 (clang-1700.6.3.2)] on darwin
Enter "help" below or click "Help" above for more information.
>>> #tuple
>>> a=(3,6.7,"hi",5+9j,True,False)
>>> print(a)
(3, 6.7, 'hi', (5+9j), True, False)
>>> type(a)
<class 'tuple'>
>>> a.index("hi")
2
>>> len(a)
6
>>> a.count(True)
1
