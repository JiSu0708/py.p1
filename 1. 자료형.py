Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
"Python's favorite food is perl"
"Python's favorite food is perl"
food = 'Python\'s favorite food is perl'
food
"Python's favorite food is perl"
"Life is too short\nYou need python"
'Life is too short\nYou need python'
"Life is too short/nYou need python"
'Life is too short/nYou need python'
'''
Life
is too short
'''
'\nLife\nis too short\n'
multiline='''
Life is too short
You need python
'''
multiline
'\nLife is too short\nYou need python\n'

==================================================================== RESTART: C:/Users/grace/AppData/Local/Programs/Python/Python311/2.py ===================================================================
'\nLife is too short\nYou need python\n'
'\nLife is too short\nYou need python\n'
a='python'
a*2
'pythonpython'
a = 'abcdefg'
len(a)
7
length(a)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    length(a)
NameError: name 'length' is not defined
len(a)
7
a = "Life is too short, You need Python"
a[0:4]
'Life'
a[:]
'Life is too short, You need Python'
a[:3]
'Lif'
"I eat %d apples." % 3
'I eat 3 apples.'
"I eat %d apples." %3
'I eat 3 apples.'
number = 10
day = 'three'
"I ate %d apples. So I was sick for %s days." %(number,day)
'I ate 10 apples. So I was sick for three days.'
"%10s" %"hi"
'        hi'
"%-10s" %"hi"
'hi        '
"%-10sjane" %"hi"
'hi        jane'
"%0.4f" 3.12345
SyntaxError: incomplete input
"%0.4f" %3.12345
'3.1235'
"%10.4f" 3.12345
SyntaxError: incomplete input
"%10.4f" %3.12345
'    3.1235'
"I ate {0} apples".format(3)
'I ate 3 apples'
"I eat {1} apples".format(1,3)
'I eat 3 apples'
number=3
"I eat {0} apples".format(number)
'I eat 3 apples'
"I eat {number} apples. So I was sick for {day} days." .format(number=10, day=3)
'I eat 10 apples. So I was sick for 3 days.'
{0:<10}.format('hi'0
               
SyntaxError: invalid syntax
{0:<10}.format('hi')
               
SyntaxError: invalid syntax
'{0:<10}'.format('hi')
               
'hi        '
"{0:<10}".format('hi')
               
'hi        '
"{0:>10}".format("hi")
               
'        hi'
"{0:^10}".format("hi")
               
'    hi    '
"{0:=^10}".format("hi")
               
'====hi===='
"{0:!<10}".format("hi")
...                
'hi!!!!!!!!'
>>> {{and}} .format()
...                
SyntaxError: invalid syntax
>>> "{{and}}" .format()
...                
'{and}'
>>> "{{and}}"
...                
'{{and}}'
>>> y=3.123456
...                
>>> "{0:10.4f}".format(y)
...                
'    3.1235'
>>> name='?????????'
...                
>>> age=30
...                
>>> f'?????? ????????? {name}??????, ????????? {age}?????????.'
...                
'?????? ????????? ???????????????, ????????? 30?????????.'
>>> f'?????? ????????? {name}??????, ????????? {age+10}?????????.'
...                
'?????? ????????? ???????????????, ????????? 40?????????.'
>>> d = {'name':?????????, 'age':30}
...                
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    d = {'name':?????????, 'age':30}
NameError: name '?????????' is not defined
>>> d = {'name':'?????????', 'age':30}
...                
>>> f'?????? ????????? {d["name"]}?????????. ????????? {d["age"]}?????????.'
...                
'?????? ????????? ??????????????????. ????????? 30?????????.'
>>> f'{"hi":<10}
...                
SyntaxError: incomplete input
>>> f'{"hi":<10}'
...                
'hi        '
>>> '{"hi":<10}'
...                
'{"hi":<10}'
>>> f'{"hi":<10}'
...                
'hi        '
>>> f'{"hi":-^10}'
...                
'----hi----'
>>> f'{{and}}'
...                
'{and}'
