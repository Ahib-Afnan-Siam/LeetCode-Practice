from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = set("aeiou")
        
        def devowel(s: str) -> str:
            s = s.lower()
            return ''.join('*' if c in vowels else c for c in s)
        
        # 1) Exact matches
        exact = set(wordlist)
        
        # 2) Case-insensitive first occurrence
        case_map = {}
        # 3) Vowel-error first occurrence (on lowercase)
        vowel_map = {}
        
        for w in wordlist:
            lw = w.lower()
            case_map.setdefault(lw, w)
            vowel_map.setdefault(devowel(w), w)
        
        ans = []
        for q in queries:
            if q in exact:
                ans.append(q)
                continue
            lq = q.lower()
            if lq in case_map:
                ans.append(case_map[lq])
                continue
            dv = devowel(q)
            ans.append(vowel_map.get(dv, ""))
        
        return ans
