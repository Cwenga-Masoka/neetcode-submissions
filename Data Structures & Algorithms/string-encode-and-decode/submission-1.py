class Solution:

    def encode(self, strs: List[str]) -> str:
        if (strs == []):
            encoded = "empty_list"
            return encoded
        else:
            encoded = ""

            for s in range(len(strs)):
                if s==0:
                    encoded += strs[s]
                else:
                    encoded += "-" + strs[s]
                    
            return encoded
        

    def decode(self, s: str) -> List[str]:
        if (s=="empty_list"):
            return []
        else:
            decoded = s.split("-")
            return decoded