# Product of Array Except Self
# I.p [4,5,7] --> [35,28,20]
# https://leetcode.com/problems/product-of-array-except-self/

# Function to calculate the product of array except self using O(n) space complexity
def productExceptSelf(nums): # O(n)
    n = len(nums)
    left = [1]*n  # Initialize left product array
    right = [1]*n  # Initialize right product array
    
    # Calculate left product array
    for i in range(1, n):
        left[i] = left[i-1]*nums[i-1]
        #print(left)
    
    # Calculate right product array
    for i in range(n-2, -1, -1):
        right[i] = right[i+1]*nums[i+1]
        #print(right)
    
    # Calculate the result by multiplying left and right product arrays
    return [left[i]*right[i] for i in range(n)] 

# Function to calculate the product of array except self using O(1) space complexity
def productExceptSelf2(nums): # O(n)
    n = len(nums)
    result = [1]*n  # Initialize result array
    
    prefix = suffix = 1  # Initialize prefix and suffix products
    
    # Calculate prefix product and store in result array
    for i in range(n):
        result[i] = prefix
        prefix = prefix * nums[i]

    # Calculate suffix product and multiply with result array
    for i in range(n-1, -1, -1):
        result[i] *= suffix
        suffix = suffix * nums[i]
    
    return result

# Test cases
print(productExceptSelf([4,5,7])) # [35,28,20]
print(productExceptSelf2([4,5,7])) # [35,28,20]