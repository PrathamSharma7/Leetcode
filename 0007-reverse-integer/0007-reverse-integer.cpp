class Solution {
public:
    int reverse(int x) {
        long int r = 0;
        while (x != 0) {
            int digit = x % 10;
            x /= 10; 
            r = r * 10 + digit;
            if (r > INT_MAX || r < INT_MIN) return 0;
        }
        return (int) r;
    }
};