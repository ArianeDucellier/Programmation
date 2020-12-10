class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while (left <= right):
            middle = (left + right) // 2
            if (nums[middle] == target):
                return middle
            if (nums[middle] > target):
                right = middle - 1
            else:
                left = middle + 1
        return -1

def mySqrt(x):
    left = 0
    right = x
    while (left < right):
        mid = (left + right) // 2
        if (mid * mid <= x) and ((mid + 1) * (mid + 1) > x):
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1