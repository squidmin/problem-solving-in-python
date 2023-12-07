"""
Given a sorted array, create a new array containing squares of all the numbers of the input array
  in the sorted order.

Example 1:
    Input: [-2, -1, 0, 2, 3]
    Output: [0, 1, 4, 4, 9]

Example 2:
    Input: [-3, -1, 0, 1, 2]
    Output: [0, 1, 1, 4, 9]


Solution
This is a straightforward question. The only trick is that we can have negative numbers in the input array,
  which will make it a bit difficult to generate the output array with squares in sorted order.
  An easier approach could be to first find the index of the first non-negative number in the array.
  After that, we can use Two Pointers to iterate the array. One pointer will move forward to iterate the
  non-negative numbers, and the other pointer will move backward to iterate the negative numbers.
  At any step, whichever number gives us a bigger square will be added to the output array.
Since the numbers at both ends can give us the largest square, an alternate approach could be to use
  two pointers starting at both ends of the input array. At any step, whichever pointer gives us the
  bigger square, we add it to the result array and move to the next/previous number according to the pointer.

Time complexity
  The above algorithm's time complexity will be O(N) as we are iterating the input array only once.
Space complexity
  The above algorithm's space complexity will also be O(N); this space will be used for the output array.
"""


def make_squares(arr):
    n = len(arr)
    squares = [0 for x in range(n)]
    highest_square_idx = n - 1
    left, right = 0, n - 1
    while left <= right:
        left_square = arr[left] * arr[left]
        right_square = arr[right] * arr[right]
        if left_square > right_square:
            squares[highest_square_idx] = left_square
            left += 1
        else:
            squares[highest_square_idx] = right_square
            right -= 1
        highest_square_idx -= 1

    return squares


def main():
    print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
    print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()
