class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictStore = dict() # store the numbers in dict such that takes O(1) time to track numbers

        for i in range(len(nums)):
            if nums[i] not in dictStore:
                dictStore[nums[i]] = i # if number doesn't exist in dict, store in dict then

            sub = target - nums[i] # To see the difference of target and current number
            if sub in dictStore and dictStore[sub] != i:
                return [dictStore[sub], i]
