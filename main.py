class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        nums2 = nums[::-1]
        nums = [sum(nums[:i]) for i in range(len(nums[:]))]
        nums2 = [sum(nums2[:i]) for i in range(len(nums2[:]))][::-1]
        return list(map(lambda x, y: abs(y - x), nums, nums2))
