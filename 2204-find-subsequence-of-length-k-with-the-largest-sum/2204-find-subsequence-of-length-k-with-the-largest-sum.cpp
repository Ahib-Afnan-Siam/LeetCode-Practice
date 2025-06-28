#include <vector>
#include <queue>
#include <algorithm>

class Solution {
public:
    std::vector<int> maxSubsequence(std::vector<int>& nums, int k) {
        auto comp = [](const std::pair<int, int>& a, const std::pair<int, int>& b) {
            if (a.first == b.first) {
                return a.second < b.second;
            }
            return a.first > b.first;
        };
        std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, decltype(comp)> pq(comp);
        
        for (int i = 0; i < nums.size(); ++i) {
            pq.push({nums[i], i});
            if (pq.size() > k) {
                pq.pop();
            }
        }
        
        std::vector<std::pair<int, int>> selected;
        while (!pq.empty()) {
            selected.push_back(pq.top());
            pq.pop();
        }
        
        std::sort(selected.begin(), selected.end(), [](const std::pair<int, int>& a, const std::pair<int, int>& b) {
            return a.second < b.second;
        });
        
        std::vector<int> result;
        for (const auto& p : selected) {
            result.push_back(p.first);
        }
        
        return result;
    }
};