modules部分還沒建置完成，勿看


BIF
======================
build in function，python內建函式

Suite
======================
python程式碼區塊，以for為例：
```python
         for i in a:
                print(i) #這裡就是Suite
```              

Module
======================
模組，我們會使用Distutils這模組發布我們自己寫的模組，模組可以用python、C、C++來寫

大致內容如下：

以名為polite的模組為例

folder:build -> 裡面放置了一個lib資料夾，lib裡放的是polite.py

folder:dist -> 

MANIFEST

polite.py -> 放置模組的函數

setup.py -> 用來設置模組的，一般來說，模組開發者會在創造完setup.py後，鍵入python setup.py sdist或是python setup.py bdist_wininst之類的指令；詳情請看指令區

```python
from distutils.core import setup

#name：模組名稱，version；版本，py_modules：模組名稱，author：作者，author_email：作者電子郵件，url：作者個人網站，description：該模組描述

setup(name='polite',version='1.0.0',py_modules=['polite'],author='bulb03',author_email=None,url=None,description='use this to be polite')
```

指令區
-------------------
1. python setup.py sdist：會創造出一份名為"模組名稱-版本號.tar.gz"的壓縮檔，EX：polite-1.0.0.tar.gz；此壓縮檔包含PKG-INFO、setup.py、模組名稱.py這三個檔案，一般使用者如果要透過此壓縮檔安裝模組，就得要解壓縮後，進到有setup.py的位址，並開啟python，輸入：python setup.py install，才能完成安裝

2. python setup.py install：如1.所說，就是安裝模組。

3. python setup.py bdlist --help-formats：則是會出現相對應的作業系統的檔案格式：

List of available distribution formats:

  --formats=rpm      RPM distribution
  
  --formats=gztar    gzip'ed tar file
  
  --formats=bztar    bzip2'ed tar file
  
  --formats=xztar    xz'ed tar file
  
  --formats=ztar     compressed tar file
  
  --formats=tar      tar file
  
  --formats=wininst  Windows executable installer
  
  --formats=zip      ZIP file
  
  --formats=msi      Microsoft Installer
  
  如果是想讓windows使用者透過exe檔直接安裝的話，一樣在setup.py的位址鍵入python setup.py bdlist_wininst，就會直接產生exe檔而不是tar.gz檔了
  
  4.


[Distutils介紹](http://blog.csdn.net/gqtcgq/article/details/49255995)
[dist簡介]()
