# -*- coding: utf-8 -*-
"""
Created on Mon May 14 10:46:51 2018

@author: sj_zheng
"""

#用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

#堆栈： 先进后出  队列：先进先出

#在Python 中 list可以实现栈的特性 .append() .pop()  后进先出 其实一个list 也可以实现队列的特性 在pop()时 pop(0)即可
# collection中的 deque  
#deque 作用很多，也可以固定大小 当.append()超出大小后 会自动删除前面老的数据

#可以实现队列的特性 .append() .popleft() 实现先进先出

#这个题可以解析为 用两个list实现一个deque ? 

#解题思路： 对于push 栈和队列的操作相同 
#对于pop 我们在入列的时候 就将其 放入一个栈1中，让另一个为空，
#然后将栈1中的元素出栈（先进后出） 进入栈2 （后-先） 然后在出栈（先-后） 实现先进先出效果

class Solution0:
    def __init__(self):
        self.l = []
        
    def push(self, node):
        self.l.append(node)
        
    def pop(self):
        return self.l.pop(0) 
        
        
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def push(self, node):
        self.stack1.append(node)

    def size(self):
        return len(self.stack1)

        
    def pop(self):
        if (self.stack1==[])&(self.stack2 == []):
            return None
        if self.stack2 == []:
            while self.stack1 != []:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


        
            

#镜像题目：用两个队列实现一个栈 
class Solution1:
    def __init__(self):
        self.queue1 =Solution()  
        self.queue2 =Solution()
    def push(self,node):
        if self.queue2.size() !=0 and self.queue1.size() == 0:
            self.queue2.push(node)
        else:
            self.queue1.push(node)
    def pop(self):
        if self.queue2.size() == 0:
            for i in range(self.queue1.size()-1):
                self.queue2.push(self.queue1.pop())
            return self.queue1.pop()
        elif self.queue1.size()==0:
            for i in range(self.queue2.size()-1):
                self.queue2.push(self.queue2.pop())
            return self.queue2.pop()            

if __name__ == '__main__':
#    s = Solution()
#    s.push(1)
#    s.push(2)
#    s.push(8)
#    s.push(10)
#    print(s.pop())
    s = Solution1()
    s.push(1)
    s.push(2)
    s.push(8)
    s.push(10)
    print(s.pop())
    s.push(88)
    print(s.pop())
    
                


