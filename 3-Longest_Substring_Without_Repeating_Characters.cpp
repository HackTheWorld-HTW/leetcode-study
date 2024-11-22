#include <vector>

class Solution {
 public:
  int lengthOfLongestSubstring(string s) {
    // Initialize the variable to store the maximum length of the substring
    int ans = 0;

    // Create a vector of size 128 (for all ASCII characters)
    // to keep track of character counts
    vector<int> count(128);

    // Use two pointers: 'l' for the left boundary and 'r' for the right boundary
    for (int l = 0, r = 0; r < s.length(); ++r) {
      // Increment the count of the current character at index 'r'
      ++count[s[r]];

      // If the current character appears more than once in the window
      while (count[s[r]] > 1)
        // Move the left pointer 'l' rightward and decrement count of 'l'
        --count[s[l++]];

      // Update the maximum length of the substring found so far
      ans = max(ans, r - l + 1);
    }

    // Return the length of the longest substring without repeating characters
    return ans;
  }
};
