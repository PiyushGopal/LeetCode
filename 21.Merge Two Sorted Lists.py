# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        newnode = ListNode()
        temp = newnode
        while(True):
            if list2 == None:
                    temp.next = list1
                    break
            elif list1 == None:
                    temp.next = list2
                    break
            else:
                if list1.val < list2.val:
                    temp.next = list1
                    list1 = list1.next
                else:
                    temp.next =  list2
                    
                    list2 = list2.next
            temp = temp.next
        return newnode.next
