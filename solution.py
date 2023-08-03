# Solutions
from typing import List
# Question 1342
class Solution1342:
    def numberOfSteps(self, num: int) -> int:
        if num != 0:
            local_num = num
            count = 0
            while local_num != 0:
                if local_num % 2 == 0:
                    local_num = local_num / 2
                    count = count + 1
                else:
                    local_num = local_num - 1
                    count = count + 1
        return count

# Question 1
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
           for k in range(len(nums)):
               sum = nums[i] + nums[k]
               if sum == target:
                   print(i, k)
                   return [i, k]


if __name__ == "__main__":
    solution = Solution1()
    steps = solution.twoSum([2, 7, 11,1, 5], 9)
    print(steps)
