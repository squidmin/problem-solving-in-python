"""
Given a string and a pattern, find out if the string contains any permutation of the pattern.

Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:
  1. abc
  2. acb
  3. bac
  4. bca
  5. cab
  6. cba

If a string has `n` distinct characters, it will have n! permutations.

Example 1:
  Input: String="oidbcaf", Pattern="abc"
  Output: true
  Explanation: The string contains "bca" which is a permutation of the given pattern.

Example 2:
  Input: String="odicf", Pattern="dc"
  Output: false
  Explanation: No permutation of the pattern is present in the given string as a substring.

Example 3:
  Input: String="bcdxabcdy", Pattern="bcdyabcdx"
  Output: true
  Explanation: Both the string and the pattern are a permutation of each other.

Example 4:
  Input: String="aaacb", Pattern="abc"
  Output: true
  Explanation: The string contains "acb" which is a permutation of the given pattern.

Time complexity:
  O(N+M), where 'N' and 'M' are the number of characters in the input string and the pattern, respectively.

Space complexity:
  O(M) since, in the worst case, the whole pattern can have distinct characters that will go into the hashmap.

Solution:
  Use a char-to-int hashmap to keep track of the unique characters.
  Add kv pairs to the char-to-int hashmap for each character in the input pattern string.
  Subsequently, iterate through the input string, checking if each of its characters has a corresponding
    key in the hash map. Store of the frequency of a character-in-common each time one is encountered.
    Hint: Use a 'matched' int variable to keep track of the number of characters matching the pattern.
  The string contains a permutation of the pattern if the number of matches equals the size of the hash map.
"""

def find_permutation(str1, pattern):
  window_start, matched = 0, 0
  char_frequency = {}

  for chr in pattern:
    if chr not in char_frequency:
      char_frequency[chr] = 0
    char_frequency[chr] += 1

  # Our goal is to match all the characters from the 'char_frequency' with the current window.
  # Try to extend the range [window_start, window_end].
  for window_end in range(len(str1)):
    right_char = str1[window_end]
    if right_char in char_frequency:
      # Decrement the frequency of matched character.
      char_frequency[right_char] -= 1
      if char_frequency[right_char] == 0:
        matched += 1

    if matched == len(char_frequency):
      return True

    # Shrink the window by one character.
    if window_end >= len(pattern) - 1:
      left_char = str1[window_start]
      window_start += 1
      if left_char in char_frequency:
        if char_frequency[left_char] == 0:
          matched -= 1
        char_frequency[left_char] += 1

  return False


def main():
  print(str(find_permutation("oidbcaf", "abc")))           # Expected output: True
  print(str(find_permutation("odicf", "dc")))              # Expected output: False
  print(str(find_permutation("bcdxabcdy", "bcdyabcdx")))   # Expected output: True
  print(str(find_permutation("aaacb", "abc")))             # Expected output: True


main()

