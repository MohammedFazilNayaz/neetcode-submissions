class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums={}
        n = len(numbers)
        for i,num in enumerate(numbers):
            b = target - num
            if b in nums:
                return [nums[b]+1,i +1]
            nums[num]=i