# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        index = 0
        nodes = [head]
        while(head.next != None):
            index += 1
            nodes.append(head.next)
            head = head.next
        return nodes[index / 2  if index % 2 == 0 else index / 2 + 1]