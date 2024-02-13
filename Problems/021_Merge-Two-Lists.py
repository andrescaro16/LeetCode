class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    
    # Time complexity: O(n)
    # Space complexity: O(n)
    def mergeTwoLists(self, list1, list2):
        mergedList = ListNode()
        current = mergedList
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 or list2

        return mergedList.next

        
        

if __name__ == '__main__':
    list1 = ListNode(2)
    list2 = ListNode(3)

    solution = Solution()
    print(solution.mergeTwoLists(list1, list2).val)
