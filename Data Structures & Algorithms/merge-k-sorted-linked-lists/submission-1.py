# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeLists(list1, list2):
            dummy = node = ListNode()

            while list1 and list2:
                if list1.val > list2.val:
                    node.next = list2
                    list2 = list2.next
                else:
                    node.next = list1
                    list1 = list1.next
                node = node.next
            
            node.next = list1 or list2
                
            return dummy.next

        if not lists:
            return None

        res = lists[0]
        for i in range(1, len(lists)):
            res = mergeLists(res, lists[i])
        
        return res