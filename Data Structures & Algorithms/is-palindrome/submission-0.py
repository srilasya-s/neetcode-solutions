class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal = s.lower()
        cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', pal)
        return (cleaned_text == cleaned_text [::-1])
             
                    
            
        