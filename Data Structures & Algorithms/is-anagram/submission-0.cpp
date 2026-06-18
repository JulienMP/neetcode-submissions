class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> s_map;
        map<char, int> t_map;
        for (char letter: s){
            ++s_map[letter];
        }
        for (char letter: t){
            ++t_map[letter];
        }
        if (s_map == t_map){
            return true;
        }
        return false;
    }
};
