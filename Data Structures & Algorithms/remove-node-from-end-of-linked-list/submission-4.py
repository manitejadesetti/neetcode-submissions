# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        total_len = 0
        while right:
            total_len += 1
            right = right.next
        
        i = 0
        n = total_len - n + 1
        print(n)
        if n == 1:
            return head.next

        while left:

            if i == n - 1:

                left.next = left.next.next if left.next else None
                break

            left = left.next
            i += 1
        
        return dummy.next


        