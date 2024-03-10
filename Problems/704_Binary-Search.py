# Time complexity: O(log n)
# Space complexity: O(1)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        leftIndex = 0
        rightIndex = len(nums) -1
        midIndex = 0

        while leftIndex <= rightIndex:
            midIndex = (leftIndex + rightIndex) // 2

            if nums[midIndex] == target:
                return midIndex
            elif nums[midIndex] < target:
                leftIndex = midIndex + 1
            else:
                rightIndex = midIndex - 1
        
        return -1
