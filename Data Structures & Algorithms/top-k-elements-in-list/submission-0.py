class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count frequencies
        count = {}
        for num in nums:
            count[num] = 1+count.get(num,0)

        # # sort arr by freq
        # arr = []
        # for num, cnt in count.items():
        #     arr.append([cnt,num])
        # arr.sort()

        # # pop top k frequent
        # res = []
        # for i in range(k):
        #     res.append(arr.pop()[1])
        # return res

        # create a min heap
        heap = []

        for num in count.keys():
            heapq.heappush(heap, (count[num], num))

            if len(heap)>k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res


        freq = []

        for num,cnt in count.items():
            freq[cnt].append(num)

        res = []

        for i in range(k):
            res.append(freq[len(freq)-i-1])

        return res


        



        
