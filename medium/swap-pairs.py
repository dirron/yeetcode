from typing import List


# Problem 24: Swap nodes in pairs (done recursively as part of recursion lesson)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


def swapPairs(head: ListNode) -> ListNode:
    def swap(a, b, c):
        if c.next is not None and c.next.next is not None:
            swap(c, c.next, c.next.next)
        b.next, c.next = c.next, b
        if a is not None:
            a.next = c

    second = None

    if head is not None:
        if head.next is not None:
            second = head.next
            swap(None, head, head.next)
        else:
            second = head

    return second


def printList(node: ListNode):
    output = []
    while node is not None:
        output.append(node)
        node = node.next
    print(output)


L = []
for i in range(4):
    new_node = ListNode(i + 1)
    L.append(new_node)

    if L[i - 1] is not None:
        L[i - 1].next = new_node

printList(L[0])
swapPairs(L[0])
printList(L[1])
