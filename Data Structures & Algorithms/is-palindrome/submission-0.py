class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = re.sub(r'[^a-zA-Z0-9]', "", s)
        front = 0
        end = len(clean_s)-1
       
        while front < end:
            if clean_s[front].lower() != clean_s[end].lower():
                return False
            front = front+1
            end = end -1

        return True
    