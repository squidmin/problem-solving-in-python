"""
Given a string with lowercase letters only, if you are allowed to replace no more than `k` letters
  with any letter, find the length of the longest substring having the same letters after replacement.

Example 1:
  Input: String="aabccbb", k=2
  Output: 5
  Explanation: Replace the two 'c' with 'b' to have the longest repeating substring "bbbbb".

Example 2:
  Input: String="abbcb", k=1
  Output: 4
  Explanation: Replace the 'c' with 'b' to have the longest repeating substring "bbbb".

Example 3:
  Input: String="abccde", k=1
  Output: 3
  Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
'''

'''
Time complexity:
  O(N), where `N` is the number of letters in the input string.

Space complexity:
  As we expect only the lower case letters in the input string, we can conclude that the space
    complexity will be O(26) to store each letter’s frequency in the HashMap, which is asymptotically
    equal to O(1).
"""

def character_replacement(str1, k):
  window_start, max_length, max_repeat_letter_count = 0, 0, 0
  frequency_map = {}

  # Try to extend the range [window_start, window_end].
  for window_end in range(len(str1)):
    right_char = str1[window_end]
    if right_char not in frequency_map:
      frequency_map[right_char] = 0
    frequency_map[right_char] += 1
    
    # We don't need to place the max_repeat_letter_count under the below `if`.
    max_repeat_letter_count = max(
      max_repeat_letter_count, frequency_map[right_char])

    # Current window size is from window_start to window_end. Overall we have a letter which is
    #   repeating 'max_repeat_letter_count' times. This means we can have a window which has one letter
    #   repeating 'max_repeat_letter_count' times and the remaining letters should be replaced.
    #   if the remaining letters are more than `k`, it is the time to shrink the window as we
    #   are not allowed to replace more than `k` letters.
    if (window_end - window_start + 1 - max_repeat_letter_count) > k:
      left_char = str1[window_start]
      frequency_map[left_char] -= 1
      window_start += 1

    max_length = max(max_length, window_end - window_start + 1)
  return max_length


def main():
  print(character_replacement("aabccbb", 2))
  print(character_replacement("abbcb", 1))
  print(character_replacement("abccde", 1))


main()
