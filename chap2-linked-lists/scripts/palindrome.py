# Check if a list is a palindrome

from LinkedListNode import *

def createLinkedList2():
    node1 = LinkedListNode('m')
    node2 = LinkedListNode('a')
    node3 = LinkedListNode('d')
    node4 = LinkedListNode('d')
    node5 = LinkedListNode('m')
    node1.nextNode = node2
    node2.nextNode = node3
    node3.nextNode = node4
    node4.nextNode = node5
    return node1

def lenOfList(head):
    count = 0
    while head != None:
        count += 1
        head = head.nextNode
    return count

def reverse(head):
    prev = None
    curr = head
    while curr != None:
        next = curr.nextNode
        if next == None:
            head  = curr
        curr.nextNode = prev
        prev = curr
        curr = next
    return head

def isPalindrome(head):
    head2 = reverse(head)
    displayList(head2)
    flag = True
    while head != None and head2 != None:
        if head.data != head2.data:
            flag = False
        head = head.nextNode
        head2 = head2.nextNode
    return flag

def isPalindromeStack(head):
    n = lenOfList(head)
    mid = n / 2
    flag = True
    stack = []
    for i in range(mid):
        stack.append(head.data)
        head = head.nextNode
    print(stack)
    if n % 2 == 1:
        head = head.nextNode
    while head != None:
        if stack.pop() != head.data:
            flag = False
            break
        head = head.nextNode
    return flag

if __name__ == "__main__":
    head = createLinkedList2()
    print(isPalindrome(head))
    print(isPalindromeStack(head))
    