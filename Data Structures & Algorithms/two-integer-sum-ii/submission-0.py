class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indices = []

        for i in range(len(numbers)):
            for j in range(len(numbers)-1, i, -1):
                if(numbers[i]+numbers[j] == target):
                    indices.append(i+1)
                    indices.append(j+1)
                    return indices