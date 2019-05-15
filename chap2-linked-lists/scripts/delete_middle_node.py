# Delete middle node from list - not first or last node
# Access given only for node to be deleted
# eg: a->b->c->d->e : delete node c : output: a->b->d->e

from LinkedListNode import * 

def createLinkedList2():
    node1 = LinkedListNode(1)
    node2 = LinkedListNode(5)
    node3 = LinkedListNode(9)
    node4 = LinkedListNode(12)
    node1.nextNode = node2
    node2.nextNode = node3
    node3.nextNode = node4
    return node1, node3

def delete_middle_node(node):
    current = node
    while current.nextNode != None:
        current.data = current.nextNode.data
        current.nextNode = current.nextNode.nextNode

head, nodeToDelete = createLinkedList2()
delete_middle_node(nodeToDelete)
displayList(head)


    