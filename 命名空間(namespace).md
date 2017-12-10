命名空間，這是什麼呢?舉個例子：

```python
import requests
import time
from selenium import webdriver
from say_hello import say_hello

print(dir())

say_hello()
```

上面的程式碼是個屬於一個小程式的，我們姑且叫它為test.py，這test.py的命名空間就叫test，它會放所有基本該有的和import進來的模組，那我們要怎麼知道它有甚麼？
在第8行的*print(dir())*就會告訴我們一切：
[**'__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', 
'__name__', '__package__', '__spec__',** 'requests', 'say_hello', 'time', 'webdriver']

有沒有注意到，我們import進來的requests、say_hello、time、webdriver全都放在這裡；**那命名空間到底有什麼作用？** 就是讓test.py可以找到這些*模組*，然後執行裡面的函數。

到這裡為止，你應該知道命名空間是啥了，但是，你肯定會發現一個*不協調*的點：
**為何一下import requests，一下from selenium import webdriver？**

**通通用import就好了不是嗎？**
沒錯，的確只要用import就可以了，這裡會這樣寫是為了說明from...import...也是可以的，那好處是什麼？那就是不用在函數前加上模組名稱

如果我是寫import say_hello，那下面的say_hello()就要改成say_hello.say_hello()

**感覺from say_hello import say_hello很方便，以後都用這種的就好了**，方便是方便，但有個缺點：如果你引進了兩個模組，其中都有個一樣名稱的函數，其中一個函數就會被蓋掉，例如：
```python
import requests
import time
from selenium import webdriver
from say_hello import say_hello
from polite import say_hello

print(dir())

say_hello()
```
就會出現以下錯誤：
*File "search_google.py", line 10, in <module>
    say_hello()
TypeError: say_hello() missing 1 required positional argument: 'i'*
        
因為polite的say_hello會蓋掉say_hello的say_hello，我最後面會放上polite和say_hello的say_hello(寫到後面都有點搞混誰是誰的say_hello...，我的命名太悲劇了QQ)

因此，最好的方式就是乖乖把模組名稱給放在函數前面，這樣就不會有問題了

補充：
-------------------
polite的：
```python
def say_hello(i):
	print(i+"say hello")
```
say_hello的：
```python
def say_hello():
	print("Hello")
```
參考
-------------------
[Django筆記 - Python的模組與套件 ](http://dokelung-blog.logdown.com/posts/243281-notes-django-python-modules-and-kits)

[github編輯](http://www.dushibaiyu.com/2014/05/github_readme-md_markdown.html)

