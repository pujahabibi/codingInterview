"""
Given an array of integers, return indices of the two numbers such that they add up to a specific
"""

def two_sums(nums, target):
    """Method 1"""
    #time complexity = O(N)
    #space complexity = O(N)
    # if len(nums) <= 1:
    #     return False

    # aux_dict = {}
    # for i in range(len(nums)):
    #     if nums[i] in aux_dict:
    #         print(aux_dict[nums[i]], i)
    #         return True
    #     else:
    #         aux_dict[target - nums[i]] = i
    # return False
    aux = []
    for i in range(len(nums)):
        if nums[i] in aux:
            print(nums[aux.index(nums[i])], nums[i])
            return True
        else:
            comp = target - nums[i]
            aux.append(comp)
    return False

    """Method 2"""
    #time complexity= O(N^2)
    #space complexity= O(1)
    # for i in range(len(nums) - 1):
    #     for j in range(i + 1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             print(nums[i],"and", nums[j])
    #             return True
    # return False



nums = [1, 2, 4, 7]
target = 8

print(two_sums(nums, target))