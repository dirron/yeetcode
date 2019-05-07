# Problem 21: Merge Two Sorted Lists (done recursively as part of lesson)
def mergeTwoLists(l1, l2):
    if l1 and l2:
        n1 = l1.next
        n2 = l2.next
        if l2.next and l1.val > l2.next.val: # push up the l1 val until it's in the correct position
            l2.next = mergeTwoLists(l1, l2.next)
            return l2
        elif l1.next and l2.val > l1.next.val: # push up the l2 val until it's in the correct position
            l1.next = mergeTwoLists(l1.next, l2)
            return l1
        elif l1.val < l2.val:
            l1.next = l2
            l2.next = mergeTwoLists(n1, n2)
            return l1
        else:
            l2.next = l1
            l1.next = mergeTwoLists(n1, n2)
            return l2
    return l1 or l2