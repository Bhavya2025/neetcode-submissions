class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> set;
        set.insert(n);
        while (n != 1) {
            int temp = 0;
            while (n != 0) {
                temp += (n % 10)*(n % 10);
                n = n / 10;
            }
            if (set.contains(temp)) return false;
            set.insert(temp);
            n = temp;
        }
        return true;
    }
};
