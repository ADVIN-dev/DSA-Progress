class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        res_sum = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if s == target:
                    return s

                if abs(s - target) < abs(res_sum - target):
                    res_sum = s

                if s < target:
                    left += 1
                else:
                    right -= 1

        return res_sum
