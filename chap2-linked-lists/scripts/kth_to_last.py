# To find kth to last element in a linkedlist
# Assumption : k = 1 is last element, k = 2 is last before and so on

import LinkedListNode

def kth_to_last(headNode, k):
    if k <= 0:
        return
    count = 0
    current = headNode
    while current != None:
        count += 1
        current = current.nextNode
    if k > count:
        return
    diff = count - k
    current = headNode
    for _ in range(diff):
        current = current.nextNode
    print("kth last : " + str(current.data))

def kth_to_last_runner(headNode, k):
    if k <= 0:
        return
    p1 = headNode
    p2 = headNode
    for _ in range(k):
        if p1 == None:
            return
        p1 = p1.nextNode
    while p1 != None:
        p1 = p1.nextNode
        p2 = p2.nextNode
    print("kth last : " + str(p2.data))

if __name__ == "__main__":
    headNode = LinkedListNode.createLinkedList()
    k = 5
    kth_to_last(headNode, k)
    kth_to_last_runner(headNode, k)
