"""
Given a string, find the length of the longest substring in it with no more than K distinct characters.
  You can assume that K is less than or equal to the length of the given string.

Example 1:
  Input: String="araaci", K=2
  Output: 4
  Explanation: The longest substring with no more than '2' distinct characters is "araa".

Example 2:
  Input: String="araaci", K=1
  Output: 2
  Explanation: The longest substring with no more than '1' distinct characters is "aa".

Example 3:
  Input: String="cbbebi", K=3
  Output: 5
  Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

Example 4:
  Input: String="cbbebi", K=10
  Output: 6
  Explanation: The longest substring with no more than '10' distinct characters is "cbbebi".


Hint:
  Use a hashmap to keep track of the number of occurrences of distinct characters.
  The length of the hash map (e.g., the number of distinct characters found) will affect the shrinking of
    the sliding window.
"""

"""
Time complexity: O(N), where N is the number of characters in the input string.
  The outer for loop runs for all characters, and the inner while loop processes each character
  only once; therefore, the time complexity of the algorithm will be O(N + N),
  which is asymptotically equivalent to O(N).

Space complexity: The algorithm’s space complexity is O(K), as it will store a maximum
  of K + 1 characters in the HashMap.
"""


def longest_substring_with_k_distinct(str_1, k):
    window_start = 0
    max_length = 0
    char_frequency = {}

    # In the following loop we'll try to extend the range [window_start, window_end].
    for window_end in range(len(str_1)):
        right_char = str_1[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        # Shrink the sliding window, until we are left with 'k' distinct characters in the char_frequency.
        while len(char_frequency) > k:
            left_char = str_1[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1  # Shrink the window.
        # Remember the maximum length so far.
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print(
        "Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))  # Expected output: 4
    print(
        "Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))  # Expected output: 2
    print(
        "Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))  # Expected output: 5


main()
