class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum,rightsum=0,sum(nums)
        for i,j in enumerate(nums):
            rightsum-=j
            if leftsum==rightsum:
                return i
            leftsum+=j
        return -1

        
