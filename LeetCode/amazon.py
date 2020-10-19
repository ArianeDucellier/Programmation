class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in seen:
                return [seen[remaining], i]
            seen[v] = i
        return []

def test_twoSum():
    """
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Input: nums = [3,2,4], target = 6
    Output: [1,2]
    Input: nums = [3,3], target = 6
    Output: [0,1]
    """
    print('Two Sum')
    s = Solution()
    result = s.twoSum([2,7,11,15], 9)
    print(result)
    result = s.twoSum([3,2,4], 6)
    print(result)
    result = s.twoSum([3,3], 6)
    print(result)
    print('\n')

if __name__ == '__main__':

    test_twoSum()
