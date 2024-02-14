# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(len(nums)):
            try:
                return [i, dic[target - nums[i]]]
            except KeyError:
                dic[nums[i]] = i
        
        return []



# Time complexity: O(n^2)
# Space complexity: O(1)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             try:
#                 if (nums.index(target - nums[i]) != i):
#                     answer = [i, nums.index(target - nums[i])]
#             except ValueError:
#                 continue
        
#         return answer

