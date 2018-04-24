#题目描述
#输入一个链表，从尾到头打印链表每个节点的值。

#主要考察 数据结构——链表

#2018-4-18

#__代表private 
#在Python中，变量名类似__xxx__的，也就是以双下划线开头，
#并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量
import sys

class Node(object):
	def __init__(self,value):
		self.value = value
		self.next = None

	def __repr__(self):

		return str(self.value)


#链表类
class LinkedList(object):
	def __init__(self):
		self.head = None
		self.length = 0

	def is_empty(self):
		return self.length == 0

	def append(self,dataOrNode):
		item = None
		if isinstance(dataOrNode,Node):
			item = dataOrNode
		else:
			item = Node(dataOrNode)

		if not self.head:
			self.head = item
			self.length += 1
		else:
			node = self.head
			while node.next:
				node = node.next
			node.next = item
			self.length += 1

	def delete(self,index):
		if self.is_empty():
			return
		if index < 0 or index >= self.length:
			return

		if index ==0:
			self.head = self.head.next
			self.length -= 1
			return
		j = 0
		node = self.head
		while node.next and j < index:
			pre_node = node
			node = node.next
			j += 1

		if j == index:
			pre_node.next = node.next
			self.length -= 1

	def insert(self,index,dataOrNode):
		if self.is_empty():
			return
		if index< 0 or index >= self.length:
			return

		item = None
		if isinstance(dataOrNode,Node):
			item = dataOrNode
		else:
			item = Node(dataOrNode)

		if index == 0:
			item.next = self.head
			self.head = item
			self.length += 1
			return
		j = 0
		node = self.head
		pre_node = self.head
		while node.next and j< index:
			pre_node = node
			node = node.next
			j += 1
		if j == index:
			item.next = node
			pre_node.next = item
			self.length += 1

	def update(self,index,data):
		if self.is_empty() or index< 0 or index >=self.length:
			return
		j = 0
		node =self.head
		while node.next and j< index:
			node = node.next
			j += 1
		if j == index:
			node.value = data

	def getItem(self,index):
		if self.is_empty() or index<0 or index >= self.length:
			return
		j = 0
		node = self.head
		while node.next and j<index:
			node = node.next
			j += 1

		return node.data
	def clear(self):
		self.head = None
		self.length = 0

	def getIndex(self,data):
		if self.is_empty():
			return
		j = 0
		node = self.head
		while node:
			if node.value == data:
				return j
			node = node.next
			j += 1
		if j == self.length:
			print("not found")
			return

	def __repr__(self):
		if self.is_empty():
			return
		node = self.head
		nlist = ''
		while node:
			nlist += str(node.value)+' ' 
			node = node.next
		return nlist

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # 返回从尾部到头部的列表值序列，例如[1,2,3]
	def printListFromTailToHead(self,listNode):
		# write code here
		out  = []
		if listNode is None:
			return 
		while listNode :
			out.append(listNode.value)
			listNode = listNode.next
		print(out)
		out.reverse() #out[::-1]
		return out

if __name__ == '__main__':
	l = sys.stdin.readline().strip()
	a = LinkedList()
	for k in l :
		if k != ' ':
			a.append(k)
		
	print(a.head)
	s  = Solution()
	print(s.printListFromTailToHead(a.head))






