class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = []
        anagrams = []
        used = [False] * len(strs)

        for i in range(len(strs)):
            sorted_strs.append(sorted(strs[i]))

        for i in range(len(strs)):
            if used[i]:
                continue
            match = []
            match.append(strs[i])
            used[i] = True
            for j in range (i+1, len(strs)):
                if not used[j] and len(sorted_strs[i])==len(sorted_strs[j]):
                    if sorted_strs[i]==sorted_strs[j]:
                        match.append(strs[j])
                        used[j] = True
            
            anagrams.append(match)

        return anagrams