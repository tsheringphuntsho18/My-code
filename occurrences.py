#case1
nums1 = [19,19,15,5,3,5,5,2]
def occurrences(nums1):
    nineteen = nums1.count(19)
    five = nums1.count(5)
    if nineteen == 2 and five >= 3:
        return True 
    else:
        return False
output1 = occurrences(nums1)
print(output1)

#case2
nums2 = [19,15,15,5,3,3,5,2]
def occurrences(nums2):
    nineteen = nums2.count(19)
    five = nums2.count(5)
    if nineteen == 2 and five >= 3:
        return True 
    else:
        return False
output2 = occurrences(nums2)
print(output2)

#case3
nums3 = [19,19,5,5,5,5,5]
def occurrences(nums3):
    nineteen = nums3.count(19)
    five = nums3.count(5)
    if nineteen == 2 and five >= 3:
        return True 
    else:
        return False
output3 = occurrences(nums3)
print(output3)