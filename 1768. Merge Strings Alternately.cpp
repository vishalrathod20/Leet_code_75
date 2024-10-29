class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string merged = "";
        int minLength = min(word1.size(), word2.size());

        for(int i = 0; i<minLength; i++){
            merged += word1[i];
            merged += word2[i];
        }

        merged.append(word1.begin()+minLength,word1.end());
        merged.append(word2.begin()+minLength,word2.end());

        return merged;
    }
};
