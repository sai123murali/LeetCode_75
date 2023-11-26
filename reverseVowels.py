class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        left_position=0
        right_position=len(s)-1
        vowels='aeiouAEIOU'

        while left_position<right_position:
            if s[left_position] in vowels and s[right_position] in vowels:

                s[left_position],s[right_position]=s[right_position],s[left_position]

                left_position+=1
                right_position-=1

            elif s[left_position] not in vowels:
                left_position+=1
            elif s[right_position]  not in vowels:
                right_position-=1

        return ''.join(s)     
