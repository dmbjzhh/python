'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit.
 Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

ex:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
        
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        i = 0
        num1, num2 = 0, 0
        while l1 != None:
            num1 += l1.val*pow(10, i)
            l1 = l1.next
            i += 1
        j = 0
        while l2 != None:
            num2 += l2.val*pow(10, j)
            l2 = l2.next
            j += 1
        sum = num1 + num2
        print sum
        head = None
        for s in str(sum):
            L = ListNode(int(s))
            L.next = head
            head = L
        return head

l1 = None
for s in str(243):
    L = ListNode(int(s))
    L.next = l1
    l1 = L

l2 = None
for s in str(465):
    L = ListNode(int(s))
    L.next = l2
    l2 = L

s = Solution()
result = s.addTwoNumbers(l1, l2)
