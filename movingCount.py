# -*- coding: utf-8 -*-
"""
Created on Wed May 16 15:45:23 2018

@author: sj_zheng
"""

#地上有一个m行和n列的方格。
#一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
#但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），
#因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？

# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        
        if rows<0 or cols<0 or threshold<0:
            return 0
        m = rows
        n = cols
        visited = [False]*(m*n) #标志 
        count = self.movingCountCore(threshold,m,n,0,0,visited)
        return count
    #核心计算方法
    def movingCountCore(self,k,m,n,i,j,visited):
        count = 0
        if self.check(k,m,n,i,j,visited):
            visited[i*n+j]=True
            count = 1 + self.movingCountCore(k,m,n,i-1,j,visited) + self.movingCountCore(k,m,n,i+1,j,visited)+self.movingCountCore(k,m,n,i,j-1,visited)+self.movingCountCore(k,m,n,i,j+1,visited)
        return count 
    
    
    #检查是否能够进入这个格子
    def check(self,k,m,n,i,j,visited):
        if i>=0 and j>=0 and i<m and j <n and not visited[i*n+j] and self.getDigitSum(i,j)<=k:
            return True
        return False            
        
    def getDigitSum(self,i,j): #得到一个点的加和值
        sum_i= sum(list(map(int,list(str(i)))))
        sum_j = sum(list(map(int,list(str(j)))))
        return sum_i + sum_j

        
        
        