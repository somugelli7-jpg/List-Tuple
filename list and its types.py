Python 3.15.0a5 (v3.15.0a5:d51cc01c197, Jan 14 2026, 10:47:57) [Clang 17.0.0 (clang-1700.6.3.2)] on darwin
Enter "help" below or click "Help" above for more information.
#list
a=[3,5.5,"python",6+9j,True,False]
print(a)
[3, 5.5, 'python', (6+9j), True, False]
type(a)
<class 'list'>
type[a]
type[[3, 5.5, 'python', (6+9j), True, False]]
b=6
type(b)
<class 'int'>
c=[6]
type(c)
<class 'list'>

#type of lists
#append
a=["python","java","c++"]
a.append(c)
a.append("c")
a
['python', 'java', 'c++', [6], 'c']
a.append("ml","ai")
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a.append("ml","ai")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["ml","ai"])
a
['python', 'java', 'c++', [6], 'c', ['ml', 'ai']]

#Extend
a.extend("html","javascript")
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a.extend("html","javascript")
TypeError: list.extend() takes exactly one argument (2 given)
a.extend(["html","css"])
a
['python', 'java', 'c++', [6], 'c', ['ml', 'ai'], 'html', 'css']
#Insert
a=["apple","banana","mango"]
a.insert(1,"kiwi")
a
['apple', 'kiwi', 'banana', 'mango']
a=["somu","lahari","together"]
a.insert[1("somu")]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a.insert[1("somu")]
TypeError: 'int' object is not callable
a.insert[1"somu"]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
TypeError: 'int' object is not callable
SyntaxError: invalid syntax

a=["somu","lahari","together"]
a.insert(1,"somu")
a
['somu', 'somu', 'lahari', 'together']
a.insert(1)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a.insert(1)
TypeError: insert expected 2 arguments, got 1
TypeError: insert expected 2 arguments, got 1
SyntaxError: invalid syntax
#index
a=["black","white","blue","purple"]
a.index("white")
1
#copy
b=["black","white","blue"]
b=a.copy
b
<built-in method copy of list object at 0x10632a180>
b=a.copy()
b
['black', 'white', 'blue', 'purple']
#sort
a=["biryani","choclates","icecreams"]
a.sort()
a
['biryani', 'choclates', 'icecreams']
b=[8,9,0,7,5,6]
b.sort()
b
[0, 5, 6, 7, 8, 9]
c=[-9,-8,-6,-5,-1,0,1]
c.sort()
c
[-9, -8, -6, -5, -1, 0, 1]
#Reverse
a=["ml","ai","ds","python"]
a.reverse()
a
['python', 'ds', 'ai', 'ml']
b.[9,9,0,0,8,8,7,7,6,6,5,5,4,4,3,3,2,2,1,1]
SyntaxError: invalid syntax
b=[0,0,9,9,8,8,7,7,6,6,5,5,4,4,3,3,2,2,1,1]
b.reverse()
b
[1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 0, 0]
#pop
a=["html","css","js"]
a.pop()
'js'
a
['html', 'css']
a.pop("css")
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    a.pop("css")
TypeError: 'str' object cannot be interpreted as an integer
a.pop(1)
'css'
a.pop(0)
'html'
a
[]
#remove
a=["hi","hello","how","how are you")
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
a=["hi","hello","how are you"]
a.remove("hi")
>>> a
['hello', 'how are you']
>>> #len
>>> a="code"
>>> len(a)
4
>>> b=["code"]
>>> len(b)
1
>>> b=["code","gnan"]
>>> len(b)
2
>>> #count
>>> a=["sky","moon","sun","cloud"]
>>> a.count()
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    a.count()
TypeError: list.count() takes exactly one argument (0 given)
>>> a.count("star")
0
>>> a.count("moon")
1
>>> #clear
>>> a=["water","drink"]
>>> a.clear()
>>> a
[]
>>> a.append("juice")
>>> a
['juice']
>>> 
