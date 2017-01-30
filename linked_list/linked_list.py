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

	# delete the first occurance of the key
	def deleteNode(self, key):

		#stire the head node
		temp = self.head

		# if head node itself hold the key to be deleted
		if(temp is not None):
			if temp.data == key:
				self.head = temp.next
				temp = None
				return

		#search for the key to be deleted 
		while(temp is not None):
			if temp.data==key:
				break
			prev = temp
			temp = temp.next

		# if key ins not present in linked list
		if temp is None:
			return

		# unlink the node from the linklist
		prev.next = temp.next

		temp = None


	# insert a new node aftera given node
	def insertAfter(self, prev_node, new_data):

		#check if previous node exist
		if prev_node is None:
			print "The given previous node must be in linkedlist"
			return

		#crete a new node with given new dat
		new_node = Node(new_data)

		# Make next of new node as next of prev node
		new_node.next = prev_node.next


		# Make next of prev_node as new Node
		prev_node.next = new_node


	#insert a new node at the end
	def append(self, new_data):

		#create a new node and put in the data
		new_node = Node(new_data)

		# is linked list ios empty
		if self.head is None:
			self.head = new_node
			return

		# Else traverse till the last node
		last = self.head
		while(last.next):
			last = last.next

		# change the next of last node
		last.next  = new_node



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
	llist.insertAfter(second, 45)
	llist.append(455)
	llist.deleteNode(48)
	llist.PrintList() # will print he list 

