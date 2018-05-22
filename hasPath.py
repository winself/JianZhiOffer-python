# -*- coding: utf-8 -*-
"""
Created on Thu May 17 09:57:45 2018

@author: sj_zheng
"""

#请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
#路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
#如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
# 例如 a b c e s f c s a d e e 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，
#因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子

#import numpy as np 

#class Solution:
#
#    
#    def hasPathCore(self,matrix,rows,cols,row,col,string,match_pathLength,used):
#        if match_pathLength == len(string): #搜索到字符串结束
#            return True
#        hasPath_flag = False
#        if (row<rows) and (col<cols) and (row>=0) and (col>=0) and (not used[row][col]) and (matrix[row][col]==string[match_pathLength]):
#            used[row][col] = True
#            match_pathLength = match_pathLength + 1
#            hasPath_flag = self.hasPathCore(matrix,rows,cols,row-1,col,string,match_pathLength,used) or self.hasPathCore(matrix,rows,cols,row+1,col,string,match_pathLength,used) or self.hasPathCore(matrix,rows,cols,row,col-1,string,match_pathLength,used) or self.hasPathCore(matrix,rows,cols,row,col+1,string,match_pathLength,used)
#            if not hasPath_flag:
#                match_pathLength = match_pathLength -1 
#                used[row][col] = False
#        return hasPath_flag
#
#                                 
#    def hasPath(self, matrix, rows, cols, path):
#        # write code here
#        #异常判断
#        if matrix==[] or rows<1 or cols<1 or path==[]:
#            return False
#         #初始化用于记录元素是都在path中已匹配 一个全False的二维数组
##         a = np.zeros(rows*cols)
##         b = a>1
##         used = b.reshape(rows,cols)
#        used = [[False]*cols for i in range(rows)]  ###!!!！
#        match_pathLength = 0
#        for i in range(rows):
#            for j in range(cols):
#                if self.hasPathCore(matrix,rows,cols,i,j,path,match_pathLength,used):
#                    return True
#        return False         


#测试时 输入 matrix 是一维的 然后根据 rows 和cols 进行操作

class Solution:

    
    def hasPathCore(self,matrix,rows,cols,row,col,string,match_pathLength,used):
        if match_pathLength == len(string): #搜索到字符串结束
            #print(match_pathLength)
            return True
        hasPath_flag = False
        if (row<rows) and (col<cols) and (row>=0) and (col>=0) and (not used[row*cols + col]) and (matrix[row*cols+col]==string[match_pathLength]):
            used[row*cols + col] = True
            #print(string[match_pathLength])
            #print(match_pathLength,row,col)
            match_pathLength = match_pathLength + 1
            hasPath_flag = self.hasPathCore(matrix,rows,cols,row-1,col,string,match_pathLength,used) or self.hasPathCore(matrix,rows,cols,row+1,col,string,match_pathLength,used) or self.hasPathCore(matrix,rows,cols,row,col-1,string,match_pathLength,used) or self.hasPathCore(matrix,rows,cols,row,col+1,string,match_pathLength,used)
            #print(hasPath_flag)
            if not hasPath_flag:
                match_pathLength = match_pathLength -1 
                #print(match_pathLength)
                used[row*cols+col] = False
        return hasPath_flag

                                 
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        #异常判断
        if matrix==[] or rows<1 or cols<1 or path==[]:
            return False
        used = [False]*(rows*cols)
        #print(used)###对每个元素进行标志
        match_pathLength = 0
        for i in range(rows):
            for j in range(cols):
                if self.hasPathCore(matrix,rows,cols,i,j,path,match_pathLength,used):
                    return True
        return False 



        

if __name__ =='__main__':
#    matrix = [['a','b','t','g'],['c','f','c','s'],['j','d','e','h']]
    matrix = "ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS"
    rows = 5
    cols = 8
    string = "SGGFIECVAASABCEHJIGQEM"
    s = Solution()
    print(s.hasPath(matrix, rows, cols, string))