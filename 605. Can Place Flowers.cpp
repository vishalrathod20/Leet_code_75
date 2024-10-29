class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int len = flowerbed.size();
        int i = 0;

        while (i < len && n > 0) {
            if (flowerbed[i] == 1) {
                // Skip the next plot since we can't plant adjacent to a flower
                i += 2;  
            } else if (i == len - 1 || flowerbed[i + 1] == 0) {
                // We can plant a flower if we're at the last plot or the next plot is empty
                n--; 
                i += 2;  // Move two positions forward since we just planted
            } else {
                // If the next plot is not empty, we need to skip to the next valid empty spot
                i += 3;  
            }
        }

        // Return true if we managed to plant all n flowers, false otherwise
        return n <= 0;  
    }
};
