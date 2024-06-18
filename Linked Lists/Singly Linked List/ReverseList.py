# https://leetcode.com/problems/reverse-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head) :
        left = None
        cur = head

        while cur is not None:
            right = cur.next
            cur.next = left
            left = cur
            cur = right
        
        head = left

        return head