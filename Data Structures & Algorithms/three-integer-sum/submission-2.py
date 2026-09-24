class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # res = set()
        # nums.sort()
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 tmp = [nums[i], nums[j], nums[k]]
        #                 res.add(tuple(tmp))
        # return [list(i) for i in res]

        nums.sort()
        res = []

      
        

        for i in range(len(nums)):

            # if first num is positive, rest all are positive
            if nums[i]>0:
                break

            # skip duplicates
            if i>0 and nums[i]==nums[i-1]:
                continue

            l = i+1
            r = len(nums)-1

            while l<r:
                threesum = nums[i]+nums[l]+nums[r]
                if threesum==0:
                    res.append([nums[i],nums[l],nums[r]])
                    # l+=1
                    # r-=1
                    # skip duplicate values
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    # while r>l and nums[r]==nums[r-1]:
                    #     r-=1
                    l+=1
                    r-=1

                elif threesum>0:
                    r-=1
                else:
                    l+=1

        return res


                

