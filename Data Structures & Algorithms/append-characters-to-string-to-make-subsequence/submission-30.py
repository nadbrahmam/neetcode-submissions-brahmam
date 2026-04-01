class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        if len(s)<=0 or len(t) <=0 : return True
        
        i,j=0,0
        stringtoadd = ""
        while i < len(t) and j < len(s):
            if t[i] == s[j]:
                i+=1
            j+=1
        
        return(len(t[i:]))
            
        
                   
        
        
