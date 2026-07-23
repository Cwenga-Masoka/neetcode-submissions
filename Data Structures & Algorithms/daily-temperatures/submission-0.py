class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []  # Stores indices of the days
        
        for i in range(n):
            # Check if current temp is warmer than the temp at the top stack index
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
                
            stack.append(i)
            
        return result
