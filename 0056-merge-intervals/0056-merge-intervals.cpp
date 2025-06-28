#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if (intervals.empty()) 
            return {};
        
        sort(intervals.begin(), intervals.end());
        
        vector<vector<int>> merged;
        int current_start = intervals[0][0];
        int current_end = intervals[0][1];
        
        for (int i = 1; i < intervals.size(); i++) {
            if (current_end >= intervals[i][0]) {
                current_end = max(current_end, intervals[i][1]);
            } else {
                merged.push_back({current_start, current_end});
                current_start = intervals[i][0];
                current_end = intervals[i][1];
            }
        }
        merged.push_back({current_start, current_end});
        
        return merged;
    }
};