from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
     # write a dictionary of elemnts:frequency
     freq=Counter(nums)
     d= dict(freq)
     #sort it in desc according to the values
     sorted_keys = sorted(freq, key=freq.get, reverse=True)
     #return first k elemnts values
     return sorted_keys[:k]
     
     