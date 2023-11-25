class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flower_helper=[0]+flowerbed+[0]
        count=0
        for i in range (1,len(flower_helper)-1):
            if flower_helper[i]==1 or flower_helper[i-1]==1 or flower_helper[i+1]==1:
                continue
            else:
                count+=1
                flower_helper[i]=1
        return count>=n
            
        
