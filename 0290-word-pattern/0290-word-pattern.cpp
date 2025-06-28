#include <vector>
#include <string>
#include <sstream>
#include <unordered_map>

class Solution {
public:
    bool wordPattern(std::string pattern, std::string s) {
        std::vector<std::string> words;
        std::stringstream ss(s);
        std::string word;
        while (ss >> word) {
            words.push_back(word);
        }
        
        if (pattern.size() != words.size()) {
            return false;
        }
        
        std::unordered_map<char, std::string> charMap;
        std::unordered_map<std::string, char> wordMap;
        
        for (int i = 0; i < pattern.size(); i++) {
            char c = pattern[i];
            std::string w = words[i];
            
            if (charMap.find(c) != charMap.end()) {
                if (charMap[c] != w) {
                    return false;
                }
            } else {
                if (wordMap.find(w) != wordMap.end()) {
                    return false;
                }
                charMap[c] = w;
                wordMap[w] = c;
            }
        }
        
        return true;
    }
};