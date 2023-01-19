"""
Given a string and a pattern, find the smallest substring in the given string which
  has all the character occurrences of the given pattern.

Example 1:
    Input: String="aabdec", Pattern="abc"
    Output: "abdec"
    Explanation: The smallest substring having all characters of the pattern is "abdec"

Example 2:
    Input: String="aabdec", Pattern="abac"
    Output: "aabdec"
    Explanation: The smallest substring having all character occurrences of the pattern is "aabdec"

Example 3:
    Input: String="abdbca", Pattern="abc"
    Output: "bca"
    Explanation: The smallest substring having all characters of the pattern is "bca".

Example 4:
    Input: String="adcad", Pattern="abc"
    Output: ""
    Explanation: No substring in the given string has all characters of the pattern.

Solution:
  Try to shrink the window while the number of pattern matches is equal to the pattern length.
"""

"""
Time complexity:
  O(N + M) where `N` and `M` are the number of characters in the input string and the pattern respectively.
  
Space complexity:
  O(M) since in the worst case, the whole pattern can have distinct characters which will go into the hashmap.
    In the worst case, we also need O(N) space for the resulting substring, which will happen when the input
    string is a permutation of the pattern.
"""


def find_substring(str1, pattern):
    window_start, matched, substr_start = 0, 0, 0
    min_length = len(str1) + 1
    char_frequency = {}

    for character in pattern:
        if character not in char_frequency:
            char_frequency[character] = 0
        char_frequency[character] += 1

    # Try to extend the range [window_start, window_end].
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] >= 0:  # Count every matching of a character.
                matched += 1

        # Shrink the window if we can, finish as soon as we remove a matched character.
        while matched == len(pattern):
            if min_length > window_end - window_start + 1:
                min_length = window_end - window_start + 1
                substr_start = window_start

            left_char = str1[window_start]
            window_start += 1
            if left_char in char_frequency:
                """
                Note that we could have redundant matching characters, therefore we'll decrement the
                  matched count only when a useful occurrence of a matched character is going out of the window
                """
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    if min_length > len(str1):
        return ""
    return str1[substr_start:substr_start + min_length]


def main():
    print(find_substring("aabdec", "abc"))
    print(find_substring("aabdec", "abac"))
    print(find_substring("abdbca", "abc"))
    print(find_substring("adcad", "abc"))


main()
