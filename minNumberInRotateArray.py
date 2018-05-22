# -*- coding: utf-8 -*-
"""
Created on Wed May 16 09:28:59 2018

@author: sj_zheng
"""

#测试用例： 3 4 5 1 2 
# 3 4 5 1 2 3
# 1 1 1 1 1
# 1 1 1 1 0
# 1 2 3 4 5

class Solution:
    def minNumberInRotateArray(self, rotateArray):  
        # write code here
        #暴力解决 O(n)
        l = len(rotateArray)
        i = 0
        if l==0:
            return None
        while i<l-1:
            if rotateArray[i+1]<rotateArray[i]: 
                return rotateArray[i+1]
            else:
                i = i+1
        if i == l-1:
            return rotateArray[0]
    
class Solution1:
    def minNumberInRotateArray(self,rotateArray):
        #二分查找 O(logn)
        l= 0
        h = len(rotateArray) - 1
        mid =l #初始化为0  # 针对 1 2 3 4
        if h == -1:
            return 0
        while rotateArray[l]>=rotateArray[h]:
            if (h-l)==1:
                mid = h
                break 
#            if l == h:
#                break
            mid = l + (h-l)//2
            if rotateArray[mid]==rotateArray[l] and rotateArray[mid]==rotateArray[h]:
                return Solution.minNumberInRotateArray(self,rotateArray)
            
            if rotateArray[mid]>=rotateArray[l]: #中间元素位于前面递增数组 最小值在它后面
                l = mid
            elif rotateArray[mid]<=rotateArray[h]:
                h = mid
        return rotateArray[mid]
                
        

if __name__ == '__main__':
#    arr = input()
#    a = list(arr.split(' '))
#    arr =list(map(int,a))
    s = Solution1()
    arr1 =[]
    res = s.minNumberInRotateArray(arr1)
    print(res)
                
                
            