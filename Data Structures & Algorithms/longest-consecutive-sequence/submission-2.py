class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        numSet=set(nums)
        for n in nums:
            if n-1 not in numSet: #checking whether the element can be the beginning of sequences
                length =0 #length of the con.sequence
                while (n+length) in numSet:
                    length+=1
                longest= max(length,longest)
        return longest
