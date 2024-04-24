"""
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Example 1:
    Input: [-3, 0, 1, 2, -1, 1, -2]
    Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
    Explanation: There are four unique triplets whose sum is equal to zero.

Example 2:
    Input: [-5, 2, -1, -2, 3]
    Output: [[-5, 2, 3], [-2, -1, 3]]
    Explanation: There are two unique triplets whose sum is equal to zero.

Solution:
    This problem follows the Two Pointers pattern and shares similarities with Pair With Target Sum.
    A couple of differences are that the input array is not sorted and instead of a pair we need to find triplets
    with a target sum of zero.
    To follow a similar approach, first, we will sort the array and then iterate through it taking one number at a time.
    Let's say during our iteration we are at number 'X', so we need to find 'Y' and 'Z' such that X + Y + X = 0.
    At this stage, our problem translates into finding a pair whose sum is equals to "-X" (as from the above equation
    Y + Z == -X).
    Another difference from Pair With Target Sum is that we need to find all the unique triplets. TO handle this,
    we have to skip any duplicate number. Since we will be sorting the array, all the duplicate numbers will be
    next to each other and are easier to skip.

Time complexity:
    Sorting the array will take O(N * log(N)). The searchPair() function will take O(N). As we are calling searchPair()
    for every number in the input array, this means that overall searchTriplets() will take O(N * log(N) + N^2),
    which is asymptotically equivalent to O(N^2).

Space complexity:
    Ignoring the space required for the output array, the space complexity of the above algorithm will be O(N)
    which is required for sorting.
"""


def search_triplets(arr):
    arr.sort()
    triplets = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i - 1]:  # Skip same element to avoid duplicate triplets.
            continue
        search_pair(arr, -arr[i], i + 1, triplets)

    return triplets


def search_pair(arr, target_sum, left, triplets):
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:  # Found the triplet.
            triplets.append([-target_sum, arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1  # Skip same element to avoid duplicate triplets.
            while left < right and arr[right] == arr[right + 1]:
                right -= 1  # Skip same element to avoid duplicate triplets.
        elif target_sum > current_sum:
            left += 1  # We need a pair with a bigger sum.
        else:
            right -= 1  # We need a pair with a smaller sum.


def main():
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
    print(search_triplets([-5, 2, -1, -2, 3]))


main()