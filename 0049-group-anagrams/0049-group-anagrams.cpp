#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groups;
        for (string& s : strs) {
            vector<int> freq(26, 0);
            for (char c : s) 
                freq[c - 'a']++;
            string key;
            for (int i = 0; i < 26; i++) 
                key += to_string(freq[i]) + '#';
            groups[key].push_back(s);
        }
        
        vector<vector<string>> result;
        for (auto& kv : groups) 
            result.push_back(kv.second);
        
        return result;
    }
};