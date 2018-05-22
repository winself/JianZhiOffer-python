# -*- coding: utf-8 -*-
"""
Created on Wed May 16 14:47:40 2018

@author: sj_zheng
"""

#大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
#n<=39


class Solution:
    def Fibonacci(self, n):
        # write code here
        res = []
        a,b = 0,1
        res.append(a)
        for i in range(1,n+1):
            a,b = b,a+b
            res.append(a)
        return res[n]

if __name__ == '__main__':
    s = Solution()
    print(s.Fibonacci(1))