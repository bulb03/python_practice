#起因：
在看udemy上的教學影片時，講者說直接用pip install web.py會出現錯誤，後來上了下面的網站，才了解原因

#原因：
web.py主要支持python2，因此，對於使用python 3的我來說，會出現一些錯誤

#安裝方法：
上web.py的github，切換至python3的branch，然後在cmd輸入：

***git clone https://github.com/webpy/webpy.git***

再cd至下載目錄，輸入：

***python ./setup.py install***

等待安裝完成

#PS：最後幾行可能會出現

...
uiltin.cpython-36.pyc
  File "C:\Users\apple\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\web\wsgiserver\ssl_builtin.py", line 43
    except ssl.SSLError, e:
                       ^
SyntaxError: invalid syntax

是正常的，因為還有部分程式碼是用python2寫的，但依舊可以使用web.py





參考網址(http://blog.csdn.net/blueheart20/article/details/75370834)
