# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        list2 = slow.next
        prev = slow.next = None

        while list2:
            next_node = list2.next

            list2.next = prev
            prev = list2
            list2 = next_node

        curr1, curr2 = head, prev
        while curr2:
            tmp1, tmp2 = curr1.next, curr2.next

            curr1.next = curr2
            curr2.next = tmp1

            curr1 = tmp1
            curr2 = tmp2
    

