# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        if head is None:
            return
        # s = set()
        # cur = head
        # s.add(cur.val)
        # while cur.next:
        #     if cur.next.val in s:
        #         cur.next = cur.next.next
        #     else:
        #         s.add(cur.next.val)
        #         cur = cur.next

        cur = head
        
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head      


