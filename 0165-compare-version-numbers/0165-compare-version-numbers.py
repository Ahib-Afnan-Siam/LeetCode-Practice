class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split versions into parts
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        # Find max length to normalize both lists
        n = max(len(v1), len(v2))
        
        # Compare revisions
        for i in range(n):
            # Get integer value of current revision (default to 0 if out of range)
            num1 = int(v1[i]) if i < len(v1) else 0
            num2 = int(v2[i]) if i < len(v2) else 0
            
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
        
        return 0
