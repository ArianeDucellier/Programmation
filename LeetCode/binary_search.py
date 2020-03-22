def search(nums, target):
    location = -1
    index = 0
    while (location == -1 and index < len(nums)):
        if (nums[index] == target):
            location = index
        index = index + 1
    return location

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