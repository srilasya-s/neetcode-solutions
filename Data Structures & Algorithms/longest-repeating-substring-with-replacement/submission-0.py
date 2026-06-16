class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #creating an emptty dictionary
        count = {}
        res = 0
        #considering 2 pointers l,r l at 0 and r will iterate
        l=0
        # frequency of most repeating chars in a window 
        max_f = 0

        for r in range(len(s)):
            # count of the element in the dictionary increases with 1 (key:value :: element : count )
            count[s[r]]= 1 + count.get(s[r],0)
            max_f = max( max_f,count[s[r]])
            # this is the key
            # the elements can be replaced as far as we have chance (k chances)
            #no need to replace chars, just updating length is required
            while (r-l+1) - max_f > k:
                count[s[l]] -= 1
                l+=1
            res = max(res, r-l+1)
        return res



            