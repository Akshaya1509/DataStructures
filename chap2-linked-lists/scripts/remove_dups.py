# remove duplicates from linked list

import LinkedListNode

def remove_dups():
    headNode = LinkedListNode.createLinkedList()
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

def remove_dups_without_buffer():
    headNode = LinkedListNode.createLinkedList()
    current = headNode
    prev = headNode
    while current != None and current.nextNode != None:
        runner = current.nextNode
        while runner != None:
            if runner.data == current.data:
                prev.nextNode = runner.nextNode
            else:
                prev = runner
            runner = runner.nextNode
        current = current.nextNode
    LinkedListNode.displayList(headNode)

if __name__ == "__main__":
    # remove_dups()
    remove_dups_without_buffer()
    