# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        rem = 0
        result = ListNode()
        temp = result

        while l1 and l2:
            val = l1.val + l2.val+rem
            if val >=10:
                rem = 1
                val= val %10
            else:
                rem=0
            result.next = ListNode(val)
            result = result.next
            l1 =l1.next
            l2 =l2.next
        
        while l1:
            val = l1.val +rem

            if val >=10:
                rem = 1
                val= val %10
            else:
                rem=0
            result.next = ListNode(val)
            result= result.next
            l1=l1.next
        
        while l2:
            val = l2.val+rem

            if val >=10:
                rem = 1
                val = val %10
            else:
                rem=0

            result.next = ListNode(val)
            result= result.next
            l2 = l2.next

        if rem == 1:
            result.next = ListNode(rem)

        return temp.next


            
