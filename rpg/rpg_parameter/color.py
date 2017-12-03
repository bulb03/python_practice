#關鍵字：PYTHON 印出的字元有顏色
#解法：http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
#註：cmd和vs code跑不出顏色，conemu可以
class bcolor:
	Black="\u001b[30;1m"
	Red="\u001b[31;1m"
	Green="\u001b[32;1m"
	Yellow="\u001b[33;1m"
	Blue="\u001b[34;1m"
	Magenta="\u001b[35;1m"
	Cyan="\u001b[36;1m"
	White="\u001b[37;1m"
	Reset="\u001b[0m"
	Bold="\u001b[1m"
	Underline="\u001b[4m"
	#如果不在最後面加上reset，cmd就會一直變成你剛設的顏色
	#使用範例：print("\u001b[95mtest\u001b[0m") => print("你要的顏色+你要的字+reset")