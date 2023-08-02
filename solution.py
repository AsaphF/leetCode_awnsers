# Solutions

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


if __name__ == "__main__":
    solution = Solution1342()
    steps = solution.numberOfSteps(128)
    print(steps)
