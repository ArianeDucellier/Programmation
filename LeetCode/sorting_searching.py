def findKthLargest(nums, k):
    """
    """
    largest = []
    i = 0
    while len(largest) < k:
        if not(nums[i] in largest):
            largest.append(nums[i])
        i = i + 1
    while i < len(nums):
        if nums[i] > max(largest):
            largest.remove(min(largest))
            largest.append(nums[i])
        i = i + 1
    return min(largest)
        