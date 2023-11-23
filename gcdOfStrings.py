class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        #first we are checking if lengths are not equal will be returning empty
        if ((str1+str2)!=(str2+str1)):
            return ""
        elif len(str1)==len(str2):
            #secondly if length os str1 and str2 are equal we can return any of string
            return str1
        else:
            #finding the gcd among the lengths of both the strings 
            return str1[:gcd(len(str1),len(str2))]

        
