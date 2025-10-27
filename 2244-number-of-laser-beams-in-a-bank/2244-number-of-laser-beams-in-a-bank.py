class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        counts = []
        for row in bank:
            device_count = row.count('1')
            if device_count > 0:
                counts.append(device_count)
        
        total_beams = 0
        for i in range(1, len(counts)):
            total_beams += counts[i-1] * counts[i]
        
        return total_beams