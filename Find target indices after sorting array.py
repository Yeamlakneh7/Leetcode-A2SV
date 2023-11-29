class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        for j in range(1, len(nums)):
            i = j
            while i - 1 >= 0 and nums[i] < nums[i - 1] :
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                i -= 1
        arr = []
        for i in range(len(nums)):
            if nums[i] == target:
                arr.append(i)
        return arr
