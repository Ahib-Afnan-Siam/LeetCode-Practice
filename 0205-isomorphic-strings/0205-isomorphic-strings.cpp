class Solution {
public:
    bool isIsomorphic(string s, string t) {
        vector<int> mapping_s(256, -1);
        vector<int> mapping_t(256, -1);
        
        for (int i = 0; i < s.size(); i++) {
            unsigned char uc_s = s[i];
            unsigned char uc_t = t[i];
            
            if (mapping_s[uc_s] == -1) {
                if (mapping_t[uc_t] != -1) {
                    return false;
                }
                mapping_s[uc_s] = uc_t;
                mapping_t[uc_t] = uc_s;
            } else {
                if (mapping_s[uc_s] != uc_t) {
                    return false;
                }
            }
        }
        
        return true;
    }
};