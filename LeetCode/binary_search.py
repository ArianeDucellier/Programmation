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

    # 69. Sqrt(x)
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x
        mid = int((left + right) / 2)
        while left < right:
            if mid * mid == x:
                return mid
            if mid * mid < x:
                left = mid + 1
            if mid * mid > x:
                right = mid - 1
            mid = int((left + right) / 2)
            print(left, right, mid)
        return mid

    # 167. Two Sum II - Input Array Is Sorted
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index1 = 0
        index2 = len(numbers) - 1
        mySum = numbers[index1] + numbers[index2]
        while mySum != target:
            if mySum > target:
                index2 = index2 - 1
            if mySum < target:
                index1 = index1 + 1
            mySum = numbers[index1] + numbers[index2]
        return (index1 + 1, index2 + 1)

    # 852. Peak Index in a Mountain Array
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        begin = 0
        end = len(arr) - 1
        while begin < end:
            center = int((begin + end) / 2)
            if arr[center] < arr[center + 1]:
                begin = center + 1
            if arr[center] > arr[center + 1]:
                end = center
        return int((begin + end) / 2)

def test_mySqrt():
    """
    Input: x = 4
    Output: 2
    Input: x = 8
    Output: 2
    """
    s = Solution()
    result = s.mySqrt(4)
    print(result)
    result = s.mySqrt(8)
    print(result)

def test_twoSum():
    """
    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    Input: numbers = [2,3,4], target = 6
    Output: [1,3]
    Input: numbers = [-1,0], target = -1
    Output: [1,2]
    """
    s = Solution()
    result = s.twoSum([2,7,11,15], 9)
    print(result)
    result = s.twoSum([2,3,4], 6)
    print(result)
    result = s.twoSum([-1,0], -1)
    print(result)

def test_peakIndexInMountainArray():
    """
    Input: arr = [0,1,0]
    Output: 1
    Input: arr = [0,2,1,0]
    Output: 1
    Input: arr = [0,10,5,2]
    Output: 1
    """
    s = Solution()
    result = s.peakIndexInMountainArray([0,1,0])
    print(result)
    result = s.peakIndexInMountainArray([0,2,1,0])
    print(result)
    result = s.peakIndexInMountainArray([0,10,5,2])
    print(result)

if __name__ == '__main__':

    test_mySqrt()
#    test_twoSum()
#    test_peakIndexInMountainArray()
