class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        final=[]
        for i in arr:
            final.append(arr.count(i))
        return len(set(final))==len(set(arr))
        
