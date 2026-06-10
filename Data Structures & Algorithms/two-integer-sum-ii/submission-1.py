class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen={}
        for i, n in enumerate(numbers):
            complement = target - n
            if complement in seen:
                return [seen[complement] + 1, i + 1]
            
            seen[n]=i
