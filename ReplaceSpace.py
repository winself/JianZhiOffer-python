# -*- coding:utf-8 -*-
#请实现一个函数，将一个字符串中的空格替换成“%20”。
#例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

# 主要需要注意的：1.list可以使用.append进行添加元素 不要总想着使用下表索引循环添加
#              2.list 如何转 str
import sys
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        l = len(s)
        #print(l)
        target = []
        j = 0
        for i in range(0,l):
        	if s[i] == ' ':
        		target.append('%')
        		target.append('20')
        		
        	else:
        		target.append(s[i]) 
        	
        return ''.join(target)

if __name__ == '__main__':
	s = sys.stdin.readline().strip()
	ss =Solution()

	print(ss.replaceSpace(s))