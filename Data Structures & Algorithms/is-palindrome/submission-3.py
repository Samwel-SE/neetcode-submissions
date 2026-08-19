class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        noSpaces = ""
        for i in s:
            if (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 48 and ord(i) <= 57):
                noSpaces = noSpaces + i

        frontPointer = 0 

        while frontPointer <= len(noSpaces) -1 -frontPointer:
            if noSpaces[frontPointer] != noSpaces[len(noSpaces) -1 -frontPointer]:
                return False
            else:
                frontPointer += 1
                continue
            
        return True 