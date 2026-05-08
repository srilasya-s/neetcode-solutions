class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            #string is encoded - ["Hello", "World!"] -> "5#Hello6#World!"
            res+=str(len(s))+'#'+s
        return res

    def decode(self, s: str) -> List[str]:
        dec=[]
        i=0
        #for each s in strs
        while i<len(s):
            j=i
            #Checks whether it's not hash
            while s[j]!="#":
                j=j+1
            # As the length is mentioned in the encoding before hash
            length = int(s[i:j])
            # word lies after hash with the length (those many characters)
            word = s[j+1 : length+j+1]
            #appending in the empty string
            dec.append(word)
            #i increments to the next string's length place
            i=j+1+length
        return dec
