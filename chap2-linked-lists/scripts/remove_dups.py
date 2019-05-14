# remove duplicates from linked list

import LinkedListNode

def createLinkedList():
    node1 = LinkedListNode.LinkedListNode(3)
    node2 = LinkedListNode.LinkedListNode(5)
    node3 = LinkedListNode.LinkedListNode(2)
    node4 = LinkedListNode.LinkedListNode(10)
    node5 = LinkedListNode.LinkedListNode(2)
    node6 = LinkedListNode.LinkedListNode(18)
    node1.nextNode = node2
    node2.nextNode = node3
    node3.nextNode = node4
    node4.nextNode = node5
    node5.nextNode = node6
    return node1

if __name__ == "__main__":
    headNode = createLinkedList()
    d = {}
    prev = None
    current = headNode
    while current != None:
        if current.data not in d:
            prev = current
            d[current.data] = 1
        else:
            prev.nextNode = current.nextNode
        current = current.nextNode
    LinkedListNode.displayList(headNode)