class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #final word op
        final_word=""
        #remainder -> if len of word1 or len of word2 is smaller we slice the word (biggest)
        remainder=""

        if(len(word1)<len(word2)):
            remainder=word2[len(word1):]
        elif(len(word2)<len(word1)):
            remainder=word1[len(word2):]

        for i in range (min(len(word1),len(word2))):
            #appending each element to final op
            final_word+=word1[i]
            final_word+=word2[i]
        final_word+=remainder
        return final_word
