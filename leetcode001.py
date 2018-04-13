# coding: utf-8
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """ def 1 """
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        
        """ def 2 """
        # for i, num in enumerate(nums):
        #     other = target - num
        #     if other in nums:
        #         j = nums.index(other)
        #         if j != i:
        #             return [i, j]
        
        """ def 3 """
        # tmp = nums
        # nums = sorted(nums)

        # i = 0
        # j = len(nums) - 1

        # while True:
        #     if nums[i] + nums[j] == target:
        #         break
        #     elif nums[i] + nums[j] < target:
        #         i += 1
        #     elif nums[i] + nums[j] > target:
        #         j -= 1

        # num_i = nums[i]
        # num_j = nums[j]
        
        # i = -1
        # j = -1

        # for k in range(len(tmp)):
        #     if tmp[k] == num_i and i == -1:
        #         i = k
        #     elif tmp[k] == num_j and j == -1:
        #         j = k

        # if i > j:
        #     i = i ^ j
        #     j = i ^ j
        #     i = i ^ j

        # return [i, j]

        """ def 4 """
        # dict_kv = {}
        # dict_vk = {}

        # for idx, num in enumerate(nums):
        #     dict_kv[idx] = num
        #     dict_vk[num] = idx

        # for k,v in dict_kv.items():
        #     other = target - v
        #     if dict_vk.has_key(other):
        #         if k != dict_vk[other]:
        #             return [k, dict_vk[other]]

        """ def 5 """
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                return [dict[nums[i]], i]
            else:
                dict[target - nums[i]] = i

print Solution().twoSum([1,3,5,7],10)