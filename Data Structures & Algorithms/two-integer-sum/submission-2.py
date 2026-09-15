class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # sorted_nums = sorted((val, idx) for idx, val in enumerate(nums))
        # i = 0
        # j = len(nums)-1
        # while i<j:
        #     if sorted_nums[i][0]+sorted_nums[j][0]==target:
        #         return sorted([sorted_nums[i][1], sorted_nums[j][1]])
        #     elif sorted_nums[i][0]+sorted_nums[j][0]<target:
        #         i+=1
        #     else:
        #         j-=1
        
        # return [0,0]

        nums_map = {}

        for i, num in enumerate(nums):
            diff = target-num
            if diff in nums_map:
                return [nums_map[diff],i]
            nums_map[num]=i
        return []

