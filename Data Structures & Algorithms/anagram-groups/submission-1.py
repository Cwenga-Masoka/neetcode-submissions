class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list) 
        for x in strs:
            count = [0]*26                    # 26 letters in alphabet
            for c in x:
                count[ord(c) - ord('a')] += 1
            
            anagrams[tuple(count)].append(x)  # make count an imutable tuple, to use as a key
        
        return list(anagrams.values())