# Problem 206: reverse linked list (done recursively as part of lesson)
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)

def printList(node: ListNode):
    output = []
    while node is not None:
        output.append(node)
        node = node.next
    print(output)

def reverseList(head: ListNode):
    if not head or not head.next:
        return head
    newHead = reverseList(head.next)
    head.next.next = head
    head.next = None
    return newHead

L = []
for i in range(4):
    new_node = ListNode(i + 1)
    L.append(new_node)

    if L[i - 1] is not None:
        L[i - 1].next = new_node

printList(L[0])
ans = reverseList(L[0])
printList(ans)