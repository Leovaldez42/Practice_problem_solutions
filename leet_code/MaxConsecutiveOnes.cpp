/* 
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
 */

// Solution
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int maxx=0, count = 0;
        for(auto i: nums) {
            if (i==1) ++count;
            else { maxx = max(maxx, count); count=0;}
        }
        return max(maxx, count);
    }
};