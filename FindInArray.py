# -*- coding:utf-8 -*-

#二维数组中的查找

#在一个二维数组中，每一行都按照从左到右递增的顺序排序，
#每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，
#判断数组中是否含有该整数。

import sys
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        #从左下角开始搜索
        m,n = len(array),len(array[0])
        i = m - 1
        j = 0
        while(i>=0) and (j<n):
        	if array[i][j] == target:
        		print('exists')
        		return
        	elif array[i][j] > target:
        		i = i - 1
        		#print('up'+ str(array[i][j]))
        	elif array[i][j] < target:
        		j = j + 1
        		#print('right'+ str(array[i][j]))
        	if 
        print('not exists')
        return 

if __name__ == '__main__':
	arr = []
	t = int(sys.stdin.readline().strip())
	
	while True:
		line = sys.stdin.readline().strip()
		if line == '':
			break
		arr.append([int(i) for i in line.split(' ')])
		
	print(arr)
	s = Solution()
	s.Find(t,arr)

			