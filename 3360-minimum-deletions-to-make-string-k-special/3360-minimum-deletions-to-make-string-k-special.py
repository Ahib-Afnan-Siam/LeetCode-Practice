from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        if not word:
            return 0
        
        cnt = Counter(word)
        freqs = list(cnt.values())
        max_freq = max(freqs)
        candidate_base = set()
        candidate_base.add(0)
        candidate_base.add(max_freq)
        distinct_freqs = set(freqs)
        
        for f in distinct_freqs:
            candidate_base.add(f)
            if f - k >= 0:
                candidate_base.add(f - k)
        
        best = float('inf')
        for base in candidate_base:
            total_del = 0
            for f in freqs:
                if f < base:
                    total_del += f
                else:
                    if f > base + k:
                        total_del += f - (base + k)
            if total_del < best:
                best = total_del
        
        return best