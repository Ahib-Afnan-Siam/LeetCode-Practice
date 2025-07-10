class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = []
        gaps.append(startTime[0])
        for i in range(1, n):
            gaps.append(startTime[i] - endTime[i-1])
        gaps.append(eventTime - endTime[n-1])
        
        prefix_top1 = [0] * (n+2)
        prefix_top2 = [0] * (n+2)
        for i in range(1, n+2):
            cur = gaps[i-1] if i-1 < len(gaps) else 0
            if cur > prefix_top1[i-1]:
                prefix_top1[i] = cur
                prefix_top2[i] = prefix_top1[i-1]
            else:
                prefix_top1[i] = prefix_top1[i-1]
                if cur > prefix_top2[i-1]:
                    prefix_top2[i] = cur
                else:
                    prefix_top2[i] = prefix_top2[i-1]
        
        suffix_top1 = [0] * (n+2)
        suffix_top2 = [0] * (n+2)
        suffix_top1[n+1] = 0
        suffix_top2[n+1] = 0
        for i in range(n, -1, -1):
            cur = gaps[i] if i < len(gaps) else 0
            if cur > suffix_top1[i+1]:
                suffix_top1[i] = cur
                suffix_top2[i] = suffix_top1[i+1]
            else:
                suffix_top1[i] = suffix_top1[i+1]
                if cur > suffix_top2[i+1]:
                    suffix_top2[i] = cur
                else:
                    suffix_top2[i] = suffix_top2[i+1]
        
        ans = 0
        for i in range(n):
            d_i = endTime[i] - startTime[i]
            merged_gap = gaps[i] + d_i + gaps[i+1]
            if i == 0:
                candidate_list = [0, 0, suffix_top1[i+2], suffix_top2[i+2], merged_gap]
            elif i == n-1:
                candidate_list = [prefix_top1[i], prefix_top2[i], 0, 0, merged_gap]
            else:
                candidate_list = [prefix_top1[i], prefix_top2[i], suffix_top1[i+2], suffix_top2[i+2], merged_gap]
            
            candidate_list.sort(reverse=True)
            M1 = candidate_list[0]
            M2 = candidate_list[1]
            
            if M1 == M2 or M2 >= d_i:
                candidate_ans = M1
            else:
                candidate_ans = max(M1 - d_i, M2)
                
            if candidate_ans > ans:
                ans = candidate_ans
                
        return ans