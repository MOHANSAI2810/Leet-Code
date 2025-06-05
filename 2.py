# Definition for singly-linked list.
#class ListNode:
 #   def __init__(self, val=0, next=None):
  #      self.val = val
   #     self.next = next

from typing import Optional

class Solution:
    def listnode_to_list(self, node: Optional[ListNode]) -> list:
        result = []
        while node:
            result.append(str(node.val))
            node = node.next
        return result

    def list_to_listnode(self, lst: list) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        for val in lst:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Convert linked lists to string lists
        l1_list = self.listnode_to_list(l1)
        l2_list = self.listnode_to_list(l2)

        # Convert to int, reverse because digits are stored in reverse order
        a = int(''.join(l1_list)[::-1])
        b = int(''.join(l2_list)[::-1])
        total = str(a + b)

        # Reverse again to get the correct linked list order
        result_digits = [int(ch) for ch in total[::-1]]

        # Convert back to ListNode
        return self.list_to_listnode(result_digits)
