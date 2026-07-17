class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = ""

        for s in range(len(strs)):
            if s==0:
                encoded += strs[s]
            else:
                encoded += "-" + strs[s]
        
        return encoded


    def decode(self, s: str) -> List[str]:
        decoded = s.split("-")
        return decoded