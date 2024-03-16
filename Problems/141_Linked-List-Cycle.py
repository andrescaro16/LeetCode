# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def hasCycle(self, head) -> bool:
        if (head and not head.next) or (not head):
            return False
        itr = head
        while (head.next and itr and itr.next and itr.next.next):
            head = head.next
            itr = itr.next.next
            if head is itr:
                return True
        return False



if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node2  # Creating the cycle

    solution = Solution()
    print(solution.hasCycle(node1))
