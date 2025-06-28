#include <vector>
#include <string>
#include <sstream>

class Solution {
public:
    std::string simplifyPath(std::string path) {
        std::vector<std::string> tokens;
        std::stringstream ss(path);
        std::string token;
        
        while (std::getline(ss, token, '/')) {
            if (token == "" || token == ".") 
                continue;
            if (token == "..") {
                if (!tokens.empty()) 
                    tokens.pop_back();
            } else {
                tokens.push_back(token);
            }
        }
        
        if (tokens.empty()) 
            return "/";
        
        std::string result;
        for (const std::string& dir : tokens) {
            result += "/" + dir;
        }
        
        return result;
    }
};