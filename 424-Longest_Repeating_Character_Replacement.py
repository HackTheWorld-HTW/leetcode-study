class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left = 0
        max_length = 0
        char_count = {}
        max_freq = 0  # Tracks the highest frequency of a single character in the window

        for right in range(len(s)):
            char = s[right]
            
            # Update the frequency count of the current character
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
            
            # Update the maximum frequency of any character in the window
            max_freq = max(max_freq, char_count[char])
            
            # Calculate the number of characters that are "wrong" in the window
            window_size = right - left + 1
            wrong_count = window_size - max_freq
            
            # If the number of "wrong" characters exceeds k, shrink the window
            if wrong_count > k:
                char_to_remove = s[left]
                char_count[char_to_remove] -= 1
                if char_count[char_to_remove] == 0:
                    del char_count[char_to_remove]
                left += 1
            
            # Update the maximum length of the valid window
            max_length = max(max_length, right - left + 1)
        
        return max_length
        