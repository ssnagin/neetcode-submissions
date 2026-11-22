class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        for num in nums:

            if num not in count:
                count[num] = 1
                continue
            
            count[num] += 1

        pairs = []

        for num in count:
            pairs.append([count[num], num])

        pairs.sort(reverse=True)

        result = []

        for num in pairs:

            if k == 0:
                break

            result.append(num[1])

            k-=1

        return result