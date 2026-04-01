class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        
        
        prevletters = ""
        i,j=0,0

        print(len(s),len(t))
        if len(s)<=0 and len(t) <=0 : 
            return False

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i+=1                                
            
            j+=1
            
        return (i == len(s))

        
        


            
            
                    
    
        