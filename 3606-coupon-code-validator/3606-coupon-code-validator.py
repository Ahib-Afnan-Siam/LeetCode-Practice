from typing import List
import re

class Solution:
    def validateCoupons(self, codes: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        # Allowed business lines in required order
        order = ["electronics", "grocery", "pharmacy", "restaurant"]
        order_index = {b: i for i, b in enumerate(order)}
        
        valid_coupons = []
        
        for i in range(len(codes)):
            # Check active status
            if not isActive[i]:
                continue
            
            # Check valid business line
            if businessLine[i] not in order_index:
                continue
            
            # Check valid code: non-empty, alphanumeric + underscore only
            if not codes[i] or not re.fullmatch(r"[A-Za-z0-9_]+", codes[i]):
                continue
            
            valid_coupons.append((order_index[businessLine[i]], codes[i]))
        
        # Sort by business line order, then lexicographically by code
        valid_coupons.sort()
        
        # Extract only the codes
        return [code for _, code in valid_coupons]
