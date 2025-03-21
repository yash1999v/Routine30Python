def bubb(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums
def selected_sort(nums):
    n=len(nums)
    for i in range(n):
        min_index = i 
        for j in range(i+1,n):
            if nums[j]<nums[min_index]:
                min_index = j
        nums[i],nums[min_index] = nums[min_index],nums[i]
    return nums


nums = [4, 3, 5, 1, 2]
print(bubb(nums))