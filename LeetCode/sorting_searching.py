def findKthLargest(nums, k):
    """
    """
    largest = nums[0 : k]
    i = 0
    while i < len(nums):
        if nums[i] >= min(largest):
            index = largest.index(min(largest))
            largest.pop(index)
            largest.append(nums[i])
        i = i + 1
    return min(largest)
        