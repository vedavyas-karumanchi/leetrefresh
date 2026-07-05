from typing import List, Optional


l1 = [2,4,3]
l2 = [5,6,4]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0)
        current = temp
        carry = 0
        while l2 != None  or  l1 != None or carry != 0:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            colsum = l1val + l2val + carry 
            carry = colsum // 10
            newNode = ListNode(colsum % 10)
            current.next = newNode
            current = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return temp.next
    def printL(self, l : ListNode):
        current = l
        while current:
            print (f"{current.val} -> ")
            current = current.next
resnode = Solution().addTwoNumbers(l1, l2)
Solution().printL(resnode)