**如題，del list到底和list=[]有什麼差異？我一開始以為是一樣的結果，直到執行了下面的程式：**

```python
m = []
n = []
file_path = "hw1_15_train.dat"
with open(file_path) as f :
	#切成一行一行
	for line in f :
		#實做m.append([float(i) for i in line.split()])的囉唆改寫：
		for i in line.split():
			n.append(i)
		m.append(n)
		del n[:]#這樣寫雖然不會把整個n刪掉，但發現m變成空的

for i in m:
	print(i)
```
後記
--------------
這是我再幫別人的PLA演算法寫註解時發現的，因為對m.append([float(i) for i in line.split()])這行很不理解，再試著用比較囉嗦的寫法改寫後偶然發現的
原本我是寫n=[]，但突然想到del，就想說可不可以用del的方式來做，查完del的說明後，寫下del n[:]，原以為這樣也可以，沒想到印出m時，全部都是空的[]

目前狀況
-------------
完全不知道為什麼，只能留下這筆記做為警惕

原完整程式碼
-------------
```python
"""不知道為什麼，del n[:]會讓m的值裡面變成[]，但n=[]的話，就不會影響到m"""

m = []
n = []
file_path = "hw1_15_train.dat"
with open(file_path) as f :
	#切成一行一行
	for line in f :
		#寫法一
		#m.append([float(i) for i in line.split()])

		"""結果：[0.99279, 0.15139, 0.27982, 0.45122, 1.0]...
		我猜，是因為[]的關係，會自動把i放進[]，再給m儲存"""

    #寫法二
       #實做m.append([float(i) for i in line.split()])的失敗囉嗦改寫
        """for i in line.split():
        m.append(float(i))"""
        #這種寫法會變成0.99279，0.15139, 0.27982, 0.45122, 1.0
        #因為line.split就會把line給一個一個切開，m.append就會一個一個i存
      
		#實做m.append([float(i) for i in line.split()])的成功囉唆改寫：
		for i in line.split():
		 n.append(i)
		m.append(n)
		
		#del n[:]#這樣寫才不會把整個n刪掉，但發現m變成空的
		
		n = []#覺得這寫法太遜，改用上面的，但上面的會讓m是空的，這個就不會

for i in m:
	print(i)
```

[參考網址： del 陳述式](https://docs.python.org.tw/3/tutorial/datastructures.html)
