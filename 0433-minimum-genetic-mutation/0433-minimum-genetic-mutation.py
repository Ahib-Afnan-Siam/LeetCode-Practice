from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene == endGene:
            return 0
        
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1
        
        queue = deque([(startGene, 0)])
        visited = set()
        visited.add(startGene)
        
        while queue:
            gene, steps = queue.popleft()
            for i in range(8):
                for c in "ACGT":
                    if gene[i] == c:
                        continue
                    new_gene = gene[:i] + c + gene[i+1:]
                    if new_gene == endGene:
                        return steps + 1
                    if new_gene in bank_set and new_gene not in visited:
                        visited.add(new_gene)
                        queue.append((new_gene, steps + 1))
        
        return -1