class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = sum(nums[:k])
        maxavg = curr_sum/k
        for n in range(len(nums) - k):
            curr_sum =  curr_sum - nums[n] + nums[k+n]
            newmax = curr_sum/k
            maxavg = max(maxavg, newmax)
        return maxavg
