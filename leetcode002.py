# coding: utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None: return l2
        if l2 is None: return l1
        
        head1 = l1
        head2 = l2
        
        while head1.next is not None or head2.next is not None:
            
            if head1.next is None:
                head1.next = ListNode(0)
            if head2.next is None:
                head2.next = ListNode(0)
        
            sum = head1.val + head2.val
            if sum >= 10:
                head1.val = sum % 10
                head1.next.val += 1
            else:
                head1.val = sum
            
            head1 = head1.next
            head2 = head2.next
            
        else:
            
            head1.val = head1.val + head2.val
            if head1.val >= 10:
                head1.val = head1.val % 10
                head1.next = ListNode(1)
            
        return l1

# test              
# l1 = ListNode(3)
# l1.next = ListNode(6)
# l1.next.next = ListNode(9)

# l2 = ListNode(2)
# l2.next = ListNode(5)
# l2.next.next = ListNode(8)

def test():
    l1 = initList([3, 6, 9]) 
    l2 = initList([2, 5, 8]) 

    rs = Solution().addTwoNumbers(l1, l2)
    show(rs)

def initList(list):
    if list is None: return ListNode(0)
    
    rs = ListNode(list[0])
    head = rs
    for i in range(1, len(list)):
        head.next = ListNode(list[i])
        head = rs.next
    return rs

def show(rs):   
    showList = []
    
    head = rs   
    while True: 
        if head.next is not None:
            showList.append(head.val)            
            head = head.next
        else:
            showList.append(head.val)
            break
    print showList

test()
