# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        vis = []
        temp = head
        while temp != None:
            if id(temp) not in vis:
                vis.append(id(temp))
                temp = temp.next
            else:
                return True
                break
    
        return False

