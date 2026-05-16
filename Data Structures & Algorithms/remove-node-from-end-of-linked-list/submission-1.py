# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp = head
        count= 0
        while tmp:
            tmp = tmp.next
            count+=1
        curr =  head
        i = 0
        n = count - n
        while curr and i <= n:
            if n == 0 and curr.next:
                curr = curr.next
                head = head.next
                break
            elif n == 0:
                curr = head = None
                break
            elif i == n-1 and curr.next:
                curr.next = curr.next.next
                break
            curr = curr.next
            i +=1
        return head

