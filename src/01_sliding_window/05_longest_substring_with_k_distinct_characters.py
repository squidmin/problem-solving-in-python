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

def non_repeat_substring(str1):
  window_start = 0
  max_length = 0
  char_index_map = {}

  # try to extend the range [windowStart, windowEnd]
  for window_end in range(len(str1)):
    right_char = str1[window_end]
    # if the map already contains the 'right_char', shrink the window from the beginning so that
    # we have only one occurrence of 'right_char'
    if right_char in char_index_map:
      # this is tricky; in the current window, we will not have any 'right_char' after its previous index
      # and if 'window_start' is already ahead of the last index of 'right_char', we'll keep 'window_start'
      window_start = max(window_start, char_index_map[right_char] + 1)
    # insert the 'right_char' into the map
    char_index_map[right_char] = window_end
    # remember the maximum length so far
    max_length = max(max_length, window_end - window_start + 1)
  return max_length


def main():
  print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abccde")))


main()
