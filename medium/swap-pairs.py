from typing import List


# Problem 24: Swap nodes in pairs (done recursively as part of recursion lesson)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


def swapPairs(head: ListNode) -> ListNode:
    if head and head.next:
        tmp = head.next
        head.next = swapPairs(tmp.next)
        tmp.next = head
        return tmp
    return head


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
printList(swapPairs(L[0]))
