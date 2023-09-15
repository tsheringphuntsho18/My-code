#Checking the lenght and fifth element occurs thrices
nums=[19,19,15,5,5,5,1,2]
def checking(nums):
    return len(nums) == 8 and nums.count(nums[4]) == 3
print(checking(nums))
