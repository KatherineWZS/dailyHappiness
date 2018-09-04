# -*- coding: utf-8 -*-

# 约瑟夫环：n个人, 从第k个开始报数(k<n)，数到m的出局。从出局者后开始从1报数，数到m出局。return 最后留下来的人的原始编号

# 初始化数组
n = 20
k = 13
m = 9

# Method 1
#list1 = [] for col in range(2)]
test = [[row for row in range(1,n+1)] for i in range(2)]
for i in range(0,n-1):
	if i == 0:
		target = (m+k-1) % n
	else:
		if m in test[1]:
			target = m
		elif m%(n-i) > 0:
			target = m%(n-i)
		elif m%(n-i) == 0:
			target = m%(n-i)+n-i

	idx = test[1].index(target)
	test[1][idx] = 'NULL'
	flag = 1
	for j in range(idx,n):
		if(test[1][j] == 'NULL'):
			pass
		else:
			test[1][j] = flag
			flag  = flag + 1
	for j in range(0,idx):
		if(test[1][j] == 'NULL'):
			pass
		else:
			test[1][j] = flag
			flag  = flag + 1	
	print '第',i,'轮: ' , test[1]

final_result = test[0][test[1].index(1)]
print 'n: %s , m: %s , k: %s' % (n,m,k) 
print  'final result~ :D ' , final_result 


# Method 2

# def josephus(n,m):
# 	if n == 2:
# 		if m%2 == 0:
# 			return 1
# 		else:
# 			return 2
# 	else:
# 		return (josephus(n-1,m) + m - 1) % n + 1


# print josephus(n,m)  , final_result




