# Python implementation of LinkedList

class LinkedListNode:
    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode

def insertAtEnd(head, newNode):
    while head.nextNode != None:
        head = head.nextNode
    head.nextNode = newNode

def displayList(head):
    while head != None:
        print(head.data)
        head = head.nextNode

def createLinkedList():
    node1 = LinkedListNode(3)
    node2 = LinkedListNode(5)
    node3 = LinkedListNode(2)
    node4 = LinkedListNode(10)
    node5 = LinkedListNode(2)
    node6 = LinkedListNode(18)
    node1.nextNode = node2
    node2.nextNode = node3
    node3.nextNode = node4
    node4.nextNode = node5
    node5.nextNode = node6
    return node1
    
if __name__ == "__main__":
    node1 = LinkedListNode("1")
    node2 = LinkedListNode("2")
    node3 = LinkedListNode("3")
    node1.nextNode = node2
    node2.nextNode = node3
    print("---------")
    displayList(node1)
    print("---------")
    insertAtEnd(node1, LinkedListNode("100"))
    print("---------")
    displayList(node1)
    print("---------")

