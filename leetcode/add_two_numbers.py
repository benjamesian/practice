#!/usr/bin/python3
# https://leetcode.com/problems/add-two-numbers/submissions/

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        out = ListNode(0)
        temp = out
        carry = 0
        while True:
            if carry:
                temp.val = 1
                carry = 0
            if l1:
                temp.val += l1.val
                l1 = l1.next
            if l2:
                temp.val += l2.val
                l2 = l2.next
            if temp.val >= 10:
                carry = 1
                temp.val -= 10
            if not (l1 or l2 or carry):
                break
            temp.next = ListNode(0)
            temp = temp.next
        return out
