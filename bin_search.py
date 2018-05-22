# -*- coding: utf-8 -*-
"""
Created on Wed May 16 11:09:38 2018

@author: sj_zheng
"""

#二分查找
#雷区很多
#1.求mid 不使用 (low+high)//2 （容易溢出错误） low + (high-low)//2
#low= mid+1 和 high=mid-1 注意 如果直接等于mid 会无法处理边界问题 出错
# 判断空的时候 大于最大或者小于最小的时候特殊情况

def find(array,a):
    high = len(array)-1
    low = 0
    mid =  low + (high-low)//2
    #大于最大的或者小于最小的
    if array == []:
        return False
    elif a>array[high] or a<array[low]:
        return False
    else:
        while low <= high  :
            if a >  array[mid]:
                low = mid+1
                mid = (low+high)//2
            elif a< array[mid]:
                high = mid -1
                mid = (low+high)//2
            else:
                return mid
    return False

if __name__=='__main__':
    l = [1,2,3,4]
    print(find(l,4))
    