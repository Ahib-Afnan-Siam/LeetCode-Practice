import bisect

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []
        prefix = ""
        for char in searchWord:
            prefix += char
            # Find the insertion point which gives the first product >= prefix
            i = bisect.bisect_left(products, prefix)
            suggestions = []
            # Check the next three products starting from i to see if they start with prefix
            for j in range(i, min(i + 3, len(products))):
                if products[j].startswith(prefix):
                    suggestions.append(products[j])
                else:
                    break
            res.append(suggestions)
        return res