class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      n=len(nums)
      res=[1]*n
      
      # product of elements that are left to the index
      prefix = 1
      for i in range(0,n):
        res[i] = prefix
        prefix*=nums[i]
      # product of elements that are right to the index
      postfix=1
      for i in range(n-1,-1,-1):
        #result = Left product X Right product
        res[i]*=postfix
        postfix*=nums[i]
      return res

        