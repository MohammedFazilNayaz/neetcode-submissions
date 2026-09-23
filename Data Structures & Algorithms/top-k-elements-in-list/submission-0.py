class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq={}
        for x in nums:
            freq[x]=freq.get(x,0) + 1
        
        sorted_item= sorted(freq.items(),key=lambda x:x[1],reverse =True)
        result=[item[0] for item in sorted_item[:k]]
        return result

                