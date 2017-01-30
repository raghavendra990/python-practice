#Node class

class Node:

	def __init__(self, data):
		self.data = data
		self.next = None


# linked list class
class LinkedList:

	#function to initialize the linke dlist onject
	def __init__(self):
		self.head = Node

	#t thios function will print hte contents of the linked lisr
	def PrintList(self):
		temp = self.head
		while(temp):
			print temp.data
			temp = temp.next

	#push the value at the first loaction
	def push(self, new_data):
		temp = Node(new_data)
		temp.next = self.head
		self.head = temp


#code execution start here

if __name__ =='__main__':

	#start with the empty liked list

	llist = LinkedList()


	llist.head = Node(1)
	second  = Node(2)
	third = Node(3)


	"thre node have been created we have refrence these blocks as first, second and third"


	"now every node has None next "

	llist.head.next  = second # link first with the secobd

	"Now `next of the first is refrence to the the second, same we have to do for second and third"

	second.next = third

	llist.push(7)

	llist.PrintList() # will print he list 

