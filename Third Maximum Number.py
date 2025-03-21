# Source: https://leetcode.com/problems/third-maximum-number/discuss/90203/Python-solution

def thirdmax(nums):
    first=second=third=float('-inf')
    for num in nums:
        if first < num:
            first,second,third=num,first,second
        elif second < num < first:
            second,third=num,second
        elif third < num < second:
            third=num
    return third if third != float('-inf') else first

print(thirdmax([3, 2, 1])) # 1
print(thirdmax([1, 2])) # 2
print(thirdmax([2, 2, 3, 1])) # 1
print(thirdmax([1, 1, 2])) # 2