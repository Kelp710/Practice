class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        if not head:
            return head

        head.next = self.removeElements(head.next, val)        
        if head.val == val:
            head = head.next

        return head
