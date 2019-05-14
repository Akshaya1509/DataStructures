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

