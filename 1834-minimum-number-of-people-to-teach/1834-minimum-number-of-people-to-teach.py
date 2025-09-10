from typing import List

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        # Convert each user's language list to a set for O(1) checks
        lang_sets = [set(langs) for langs in languages]  # users are 1-indexed in friendships
        
        # Step 1: find users who are in at least one "blocked" friendship
        need = set()
        for u, v in friendships:
            u -= 1; v -= 1  # to 0-index
            if lang_sets[u].isdisjoint(lang_sets[v]):  # they share no language
                need.add(u)
                need.add(v)
        
        if not need:
            return 0
        
        # Step 3: count, for each language ℓ, how many users in `need` already know ℓ
        counts = [0] * (n + 1)  # languages are 1..n
        for u in need:
            for ℓ in lang_sets[u]:
                counts[ℓ] += 1
        
        # Step 4: choose the language that maximizes existing knowledge within `need`
        best = max(counts[1:])  # ignore index 0
        return len(need) - best
