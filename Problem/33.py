def search(nums, target):
    def binary_search(arr, target):
        low = 0
        high = len(arr)-1
        mid = (high + low)//2
        if len(arr) == 0:
            return -1

        while low <= high:
            if arr[mid] < target:
                low = mid + 1
            elif arr[mid] > target:
                high = mid - 1
            else:
                return mid
            mid = (high + low)//2
        return -1
    
    low = 0
    high = len(nums)-1
    mid = (high + low)//2
    if nums[low] > nums[high]:
        while nums[low] > nums[high]:
            mid = (high + low)//2
            if nums[mid] > nums[high]:
                    low = mid + 1
            else:
                    high = mid
        first_half = binary_search(nums[low:], target)
        second_half = binary_search(nums[:low], target)
        if first_half != -1:
            return max(first_half + low, second_half)
        elif second_half != -1:
            return second_half
        else:
            return -1
    else:
        return binary_search(nums, target)
    
print(search([5,1,3], 5))