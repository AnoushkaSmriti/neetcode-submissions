class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prod = 1
        count0 = 0
        for num in nums:
            if num == 0:
                count0+=1
                continue
            prod = prod*num
        # print(prod)

        for num in nums:
            # Two or more zeros
            if count0 > 1:
                return [0] * len(nums)

            if count0==1:
                if num == 0:
                    output.append(prod)
                else:
                    output.append(0)
            else:
                output.append((prod//num))

        return output

