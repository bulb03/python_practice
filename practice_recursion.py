"""
此函數只是要做印出有list的list，原理就是遞迴，
如果遇到list，就繼續呼叫print_list，直到沒有list為止
"""
"""
疑問：到底要不要寫return print_list(i)，因為結果一樣
實測一：
	將print_list(i)改成return print_list()
	print(i)改成return i
	print_list(b)改成print(print_list(b))
	得到結果：只有1
因為return完1就會結束了(函數就是這樣)
實測二：
	將b改成[[1,2],3,[4,[5,6]]]
	結果：同實測一

結論：
	既然都會print出來了，那有沒有return都沒差，因為就算會return，也只是return print_list()
	回去而已，我猜，是長這樣：1,2,3,print_list([4,[5,6]]) => 1,2,3,4,print_list([5,6])
	=>1,2,3,4,5,6
	而且，這函數不能用print(print_list(b))的方式來做，因為如同實測一和二，return完一個就結束了

"""
def print_list(ex):
	for i in ex:
		#遇到list
		if isinstance(i,list):
			#呼叫print_list
			#return print_list(i)
			print_list(i)
		#遇到不是list
		else:
			#直接印出來
			print(i)



b = [1,2,3,[4,[5,6]]]
print_list(b)

"""
結果：
1
2
3
4
5
6
"""

"""
這只是用來驗證為何需要return而已，結論也很簡單，因為他會一路呼叫到i==1或0的時候，再一路乘回來
如：return 5*cal(4) => return 5*4*cal(3) => return 5*4*3*cal(2) => return 5*4*3*2*cal(1) => return 5*4*3*2*1
"""
def cal(i):
	if i == 1 or i == 0:
		return i
	else:
		return i*cal(i-1)


data = input(">>>Please enter the number of !(EX:5!):")
print(cal(int(data)))
