"""
Given an array of sorted numbers, remove all duplicate number instances from it in-place,
  such that each element appears only once. The relative order of the elements should
  be kept the same, and you should not use any extra space so that the solution has a
  space complexity of O(1).
Move all the unique elements at the beginning of the array and after moving return the
  length of the subarray that has no duplicate in it.

Example 1:
    Input: [2, 3, 3, 3, 6, 9, 9]
    Output: 4
    Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

Example 2:
    Input: [2, 2, 2, 11]
    Output: 2
    Explanation: The first two elements after removing the duplicates will be [2, 11].
"""


def remove_duplicates_bruteforce(arr):
    """
    Time complexity:
      O(N), where `N` is the total number of elements in the given array.

    Space complexity:
      Constant space, O(1).
    """
    next_non_duplicate = 1  # Index of the next non-duplicate element.

    i = 0
    while i < len(arr):
        if arr[next_non_duplicate - 1] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1
        i += 1

    return next_non_duplicate


def remove_duplicates_optimized(arr, key):
    """
    Time and space complexity:
      O(N), where `N` is the total number of elements in the given array.
    """
    next_element = 0  # Index of the next element which is not 'key'.
    for i in range(len(arr)):
        if arr[i] != key:
            arr[next_element] = arr[i]
            next_element += 1

    return next_element


def main():
    print("Array new length: " +
          str(remove_duplicates_optimized([3, 2, 3, 6, 3, 10, 9, 3], 3)))
    print("Array new length: " +
          str(remove_duplicates_optimized([2, 11, 2, 2, 1], 2)))


main()
