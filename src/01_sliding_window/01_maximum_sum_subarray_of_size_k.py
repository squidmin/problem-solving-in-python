"""
Given an array of positive numbers and a positive number `k`, find the maximum sum of
  its contiguous subarrays of size `k`.

Example 1:
Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Example 2:
Input: [2, 3, 4, 1, 5], k=2
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
"""

"""
Time complexity: O(N * K)
  where N is the total number of elements in the given array.

Space complexity: O(1)
"""


def max_sum_subarray_of_size_k_brute_force(k, arr) -> int:
    max_sum = 0
    window_sum = 0
    for i in range(len(arr) - k + 1):
        window_sum = 0
        for j in range(i, i + k):
            window_sum += arr[j]
        max_sum = max(max_sum, window_sum)

    return max_sum


"""
Time complexity: O(N)
  where N is the total number of elements in the given array.

Space complexity: O(1)
"""


def max_sum_subarray_of_size_k_optimized(k, arr):
    """Finds the maximum sum of contiguous subarrays of size `k` in an array of positive numbers.

  Parameters
  ----------
  k : int
      A target size for contiguous subarrays in `arr`.
  arr : list
      The input array across which the sliding window traverses.

  Returns
  -------
  int
      The maximum sum of contiguous subarrays of size `k`.
  """

    max_sum, window_sum = 0, 0
    window_start = 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if (window_end >= k - 1):
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1
    return max_sum


def main():
    print("Maximum sum of a subarray of size K (brute force): " + str(
        max_sum_subarray_of_size_k_brute_force(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K (brute force): " + str(
        max_sum_subarray_of_size_k_brute_force(2, [2, 3, 4, 1, 5])))
    print("Maximum sum of a subarray of size K (optimized): " + str(
        max_sum_subarray_of_size_k_optimized(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K (optimized): " + str(
        max_sum_subarray_of_size_k_optimized(2, [2, 3, 4, 1, 5])))


main()
