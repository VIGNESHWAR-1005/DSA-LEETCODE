class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        unique_types = len(set(candyType))
        return min(unique_types, len(candyType)//2)

    candyType = [1,1,2,2,3,3]
  
        