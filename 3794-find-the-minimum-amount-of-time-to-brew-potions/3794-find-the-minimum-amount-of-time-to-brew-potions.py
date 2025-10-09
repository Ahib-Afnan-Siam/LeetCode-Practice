from typing import List

class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        # prefix sums of skill: SKpref[i] = sum_{k=0..i} skill[k]
        SKpref = [0] * n
        s = 0
        for i, v in enumerate(skill):
            s += v
            SKpref[i] = s

        # S[j] = start time of potion j on wizard 0
        S = [0] * m
        # S[0] = 0 (start first potion at time 0)
        for j in range(1, m):
            prev = S[j-1]
            mj = mana[j]
            mj1 = mana[j-1]
            mx = -10**30
            # maximize over machines i
            for i in range(n):
                # pref[i][j-1] = SKpref[i] * mj1
                # pref[i-1][j] = SKpref[i-1] * mj  (SKpref[-1] treated as 0)
                a = SKpref[i] * mj1
                b = SKpref[i-1] * mj if i > 0 else 0
                val = prev + a - b
                if val > mx:
                    mx = val
            S[j] = mx

        # makespan = start of last potion + total processing of last potion
        return S[m-1] + SKpref[n-1] * mana[m-1]
