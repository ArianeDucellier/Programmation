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

    # k-th largest element
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        largest = nums[0:k]
        for i in range(k, len(nums)):
            if nums[i] > min(largest):
                index = largest.index(min(largest))
                largest.pop(index)
                largest.append(nums[i])
        return (min(largest))

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.keys = []
        self.values = []
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.keys:
            index = self.keys.index(key)
            self.keys.append(self.keys.pop(index))
            self.values.append(self.values.pop(index))
            return self.values[-1]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.keys:
            index = self.keys.index(key)
            self.values[index] = value
            self.keys.append(self.keys.pop(index))
            self.values.append(self.values.pop(index))
        else:
            if len(self.keys) == self.capacity:
                del self.keys[0]
                del self.values[0]
            self.keys.append(key)
            self.values.append(value)
        return None

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

def test_findKthLargest():
    """
    Input: nums = [3,2,1,5,6,4], k = 2
    Output: 5
    Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
    Output: 4
    """
    print('findKthLargest')
    s = Solution()
    result = s.findKthLargest([3,2,1,5,6,4], 2)
    print(result)
    result = s.findKthLargest([3,2,3,1,2,4,5,5,6], 4)
    print(result)

if __name__ == '__main__':

#    test_twoSum()
    test_findKthLargest()
