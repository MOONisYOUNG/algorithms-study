from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for cur_idx, cur_t in enumerate(temperatures):
            while stack and cur_t > temperatures[stack[-1]]:
                before_idx = stack.pop()
                answer[before_idx] = cur_idx - before_idx
            stack.append(cur_idx)

        return answer