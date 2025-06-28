#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        if (k == 0) 
            return false;
        unordered_set<int> window;
        for (int i = 0; i < nums.size(); i++) {
            if (window.find(nums[i]) != window.end()) {
                return true;
            }
            window.insert(nums[i]);
            if (i >= k) {
                window.erase(nums[i - k]);
            }
        }
        return false;
    }
};