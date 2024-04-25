# SINGLY LINKED LIST
class Node:
    def _init_(self, data):
        self.data = data 
        self.next = None
 
def printLinkedList(head):
    curr = head
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.next
    print()
 
def insertAtEndOfTail(head, ele):
    # Expectation is:
    # 1. It should create a new block with data as ele
    # 2. It should add this block at the end of insertAtEndOfTail
    # 3. Finally this function should return head of linked list
 
    # fulfilling expectation-1
    newBlock = Node(ele)
    # fulfilling expectation-2
    if head == None:
        return newBlock
    # 11 --> 22 --> 33 --> 44 --> 55 --> None
    curr = head 
    while curr.next != None:
        curr = curr.next 
    curr.next = newBlock
    # fulfilling expectation-3
    return head
 
 
# 11 --> 22 --> 33 --> 44 --> None
# head
 
# 1. Block creation for new value
# 2. Attaching link 
# 3. Change the head
 
def insertNodeAtHeadOfLinkedList(head, ele):
    # Expectation is:
    # 1. It should create a new block with data as ele
    # 2. It should add this block at the front of Linkedlist
    # 3. Finally this function should return head of linked list
    newBlock = Node(ele)
    if head == None:
        return newBlock
    newBlock.next = head 
    return newBlock
 
def insertAtSpecificPosition(head, position, value):
    newBlock = Node(value)
    if position == 1:
        newBlock.next = head 
        return newBlock
 
    index = 1 
    curr = head 
    while index != position - 1:
        curr = curr.next 
        index += 1 
 
    newBlock.next = curr.next
    curr.next = newBlock
    return head
 
# 10 --> 22 --> 45 --> 67 --> 32 --> 78 --> None
# 1      2       3     4      5      6 
 
# 67 -> 790 --> 32 --> 78 --> None
 
# (1, 790)
# (position = 5)
 
def deleteTailNode(head):
    curr=head
    previous=None
    while curr.next != None:
        previous = curr
        curr=curr.next
    previous.next=None
    return head
   
# 2500
# (1876, 23)
# (position, value)
# head to (position - 1)
 
 
 
# head, position, value
 
# 1. creating newBlock for given value
# 2. 
# 10 --> 22 --> 45 --> 67 --> 790 ---> 32 --> 78 --> None
# 1      2       3     4      5      6       
 
l = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]
head = None 
for ele in l:
    # head = insertAtEndOfTail(head, ele)
    head = insertNodeAtHeadOfLinkedList(head, ele)
 
printLinkedList(head)
# head = insertAtSpecificPosition(head, 1, 1009)
head = deleteTailNode(head)
printLinkedList(head)

head = deleteTailNode(head)
printLinkedList(head)

head = deleteTailNode(head)
printLinkedList(head)









# DELETION IN SINGLY LINKED LIST

class Node:
    def _init_(self,data):
        self.data=data
        self.next=None
 
def insertAtEndOfTail(head, ele):
    newBlock = Node(ele)
    if head == None:
        return newBlock
    curr = head 
    while curr.next != None:
        curr = curr.next 
    curr.next = newBlock
    return head
 
def printlist(head):
    # below line of code is assigning head to curr variable
    curr=head
 
    # below line is checking whether curr reached none or not
    while curr!=None:
 
        # here we are trying to print data in curr pointer 
        print(curr.data,end=" ")
        curr=curr.next
    print()
 
 
# 1. Deleting head node in a linked list
# 2. Deleting node at specific position in linked list
 
# Before deletion
# 21 --> 45 --> 100 --> 12 --> 78 --> 56 --> None 
# 1       2      3       4      5      6 
 
# position = 4
 
# 9500 
# 5631 
 
def deleteHeadNodeInLinkedList(head):
    # delete link between first and second node
    # change the head to newHead
    if head == None:
        return None 
 
    secondNode = head.next 
    head.next = None 
    return secondNode
 
# After deletion
# 21 --> 45 --> 100 --> 78 --> 56 --> None 
# 1       2      3       4      5       
 
 
def deleteNodeAtSpecificPosition(head, position):
    if position == 1:
        return deleteHeadNodeInLinkedList(head)
    curr = head 
    index = 1 
    while index != position - 1:
        curr = curr.next 
        index += 1 
    # curr --> points to (position - 1)
    mainNode = curr.next 
    # mainNode --> points to (position)
    nextNode = mainNode.next 
    # nextNode --> points to (position + 1)
    # 5630 --> None 
    # 5631 --> None 
    # 5632
    # 5630 --> 5632
    mainNode.next = None 
    curr.next = None 
    curr.next = nextNode 
    return head
 
# 21 --> None 
# 45 --> 100 --> 12 
 
n=int(input())
l=list(map(int,input().split()))
head=None
for ele in l:
    head=insertAtEndOfTail(head,ele)
printlist(head)
head = deleteHeadNodeInLinkedList(head)
printlist(head)
 
head = deleteHeadNodeInLinkedList(head)
printlist(head
