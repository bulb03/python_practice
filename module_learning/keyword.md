簡介
==============
看那些字是python關鍵字

函數
==============

*keyword.iskeyword(s)*
-----------------------
如果s是關鍵字，就回傳True；

EX：

keyword.iskeyword('True') ==> True

keyword.iskeyword('status') ==> False

*keyword.kwlist*
-----------------------
直接下keyword.kwlist即可顯示所有python關鍵字

EX：

*>>>k.kwlist*

*['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']*
