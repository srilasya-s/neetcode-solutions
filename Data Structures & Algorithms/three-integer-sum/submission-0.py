class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s_nums= sorted(nums)
        res=[]

        for i in range (len(s_nums)) :
            #to avoid duplicates
            if i>0 and s_nums[i]==s_nums[i-1]:
                continue
            #declaring pointers
            left = i+1
            right = len(nums)-1
            # condition and requirement
            while left < right:
               total = s_nums[i]+s_nums[left]+s_nums[right]
               #logic
               if total==0:
                res.append([s_nums[i],s_nums[left],s_nums[right]])

                while left < right and s_nums[left]==s_nums[left+1]:
                  left += 1
                while left < right and s_nums[right] == s_nums[right-1]:
                 right -= 1
            
                left+=1
                right-=1

               elif total < 0:
                 left+=1
               else:
                right-=1
        return res
       