# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        
        for i in range(1,len(lists)):
            lists[i] = self.merge(lists[i],lists[i-1])

        return lists[-1]




    def merge(self,list1,list2):
        res = ListNode(-99999)
        temp = res
        
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
                
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next

        if list1 != None:
            temp.next = list1
        
        if list2 != None:
            temp.next = list2
        
        return res.next