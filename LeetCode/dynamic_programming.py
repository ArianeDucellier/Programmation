def maxProfit(prices):
    """
    """
    buy = [prices[0]]
    sell = []
    for price in prices[1:]:
        # Do we buy?
        if price < min(buy):
            if len(sell) == 0:
                buy[0] = price
            else:
                buy.append(price)
        # Do we sell?
        for i in range(0, len(buy)):
            if price > buy[i]:
                if i + 1 > len(sell):
                    sell.append(price)
                else:
                    if price > sell[i]:
                        sell[i] = price
    profit = []
    if len(sell) == 0:
        return None
    else:
        for i in range(0, min(len(buy), len(sell))):
            profit.append(sell[i] - buy[i])
        return max(profit)

# 53. Maximum Subarray
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        my_sum = 0
        sum_max = nums[0]
        value_max = nums[0]
        for num in nums:
            my_sum = my_sum + num
            if my_sum < 0:
                my_sum = 0
            if my_sum > sum_max:
                sum_max = my_sum
            if num > value_max:
                value_max = num
        if sum_max == 0:
            return value_max
        else:
            return sum_max

def test_maxSubArray():
    """
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Input: nums = [1]
    Output: 1
    Input: nums = [5,4,-1,7,8]
    Output: 23
    """
    s = Solution()
    result = s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(result)
    result = s.maxSubArray([1])
    print(result)
    result = s.maxSubArray([5,4,-1,7,8])
    print(result)

if __name__ == '__main__':

    test_maxSubArray()
