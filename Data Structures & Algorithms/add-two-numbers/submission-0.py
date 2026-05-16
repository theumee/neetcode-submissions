# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        listSum = self.reverseListNum(l1) + self.reverseListNum(l2)
        dummy = node = ListNode()
        while listSum:
            tmp = listSum % 10
            listSum //= 10
            node.val = tmp
            if listSum:
                n = ListNode(tmp)
                node.next = n
                node = node.next
        return dummy
    

    
    def reverseListNum(self, head:Optional[ListNode]):
        curr = head
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        node = prev
        num = ""
        while node:
            num += str(node.val)
            node = node.next
        return int(num)