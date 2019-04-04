# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res_list = []
        while l1 != None and l2 != None:
            res = l1.val + l2.val
            if res >= 10:
                if l1.next == None:
                    temp_node = ListNode(1)
                    temp_node.next = None
                    l1.next = temp_node
                    res -= 10
                else:
                    l1.next.val += 1
                    res -= 10
            l1 = l1.next
            l2 = l2.next
            node = ListNode(res)
            node.next = None
            res_list.append(node)
            
        if l1 == None:
            while l2 != None:
                if l2.val >= 10:
                    if l2.next == None:
                        a = ListNode(1)
                        a.next = None
                        l2.val -= 10
                        l2.next = a
                    else:
                        l2.next.val += 1
                        l2.val -= 10
                    res_list.append(l2)
                    l2 = l2.next
                else:
                    res_list.append(l2)
                    l2 =l2.next
        if l2 == None:
            while l1 != None:
                if l1.val >= 10:
                    if l1.next == None:
                        a = ListNode(1)
                        a.next = None
                        l1.val -= 10
                        l1.next = a
                    else:
                        l1.next.val += 1
                        l1.val -= 10
                    res_list.append(l1)
                    l1 = l1.next
                else:
                    res_list.append(l1)
                    l1 =l1.next
        for i in range(0,len(res_list)):
            if i == len(res_list)-1:
                res_list[i].next = None
            else:
                res_list[i].next = res_list[i+1]
        return res_list[0]
                