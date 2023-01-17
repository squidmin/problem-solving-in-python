import math

'''
Problem statement
Given an array of positive numbers and a positive number `S,` find the length of the smallest
  contiguous subarray whose sum is greater than or equal to `S`.
  Return 0 if no such subarray exists.

Example 1:
    Input: [2, 1, 5, 2, 3, 2], S=7
    Output: 2
    Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].

Example 2:
    Input: [2, 1, 5, 2, 8], S=7
    Output: 1
    Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

Example 3:
    Input: [3, 4, 1, 1, 6], S=8
    Output: 3
    Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1]
    or [1, 1, 6].
'''

'''
Time complexity: The outer for loop runs for all elements, and the inner while loop processes
  each element only once; therefore, the time complexity of the algorithm will be O(N+N),
  which is asymptotically equivalent to O(N).

Space complexity: O(1)
'''

def smallest_subarray_sum(s, arr):
  """Finds the length of the smallest contiguous subarray whose sum is greater than or equal to `S`.

  Parameters
  ----------
  s : int
      A target sum against which the sum of each contiguous subarray is compared.
  arr : list
      The input array across which the sliding window traverses.

  Returns
  -------
  int
      The length of the smallest contiguous subarray whose sum is greater than or equal to `S`.

  Examples
  --------
  >>> smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2])
  2

  >>> smallest_subarray_sum(8, [3, 4, 1, 1, 6])
  3
  """

  min_length = math.inf
  window_sum = 0
  window_start = 0
  for window_end in range(0, len(arr)):
    window_sum += arr[window_end]  # add the next element
    # shrink the window as small as possible until the 'window_sum' is smaller than 's'
    while window_sum >= s:
      min_length = min(min_length, window_end - window_start + 1)
      window_sum -= arr[window_start]
      window_start += 1
      
  if min_length == math.inf:
    return 0
  return min_length


def main():
  print("Smallest subarray length: " + str(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2])))
  print("Smallest subarray length: " + str(smallest_subarray_sum(8, [3, 4, 1, 1, 6])))
  print("Smallest subarray length: " + str(smallest_subarray_sum(8, [2, 1, 5, 2, 3, 2])))

main()
