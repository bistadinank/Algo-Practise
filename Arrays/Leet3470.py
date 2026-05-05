from typing import List


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return -1

        ans = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    for k in range(j + 1, n):
                        if nums[k] == nums[i]:
                            # Total pairwise distance: (b-a) + (c-b) + (c-a) = 2*(c-a)
                            ans = min(ans, 2 * (k - i))
                            break  # larger k can only increase cost

        return -1 if ans == float('inf') else ans
