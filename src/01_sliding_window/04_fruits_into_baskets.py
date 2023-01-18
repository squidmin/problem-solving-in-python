'''
You are visiting a farm to collect fruits. The farm has a single row of
  fruit trees. You will be given two baskets, and your goal is to pick as
  many fruits as possible to be placed in the given baskets.

You will be given an array of characters where each character represents a
  fruit tree. The farm has the following restrictions:

  1. Each basket can have only one type of fruit. There is no limit to how many
       fruits a basket can hold.
  2. You can start with any tree, but you can't skip a tree once you have started.
  3. You will pick exactly one fruit from every tree until you cannot; i.e.,
       you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both baskets.


Example 1:
  Input: Fruit=['A', 'B', 'C', 'A', 'C']
  Output: 3
  Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Example 2:
  Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
  Output: 5
  Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
  This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

Hint: Use a hashmap to keep track of the occurrences of two distinct types of fruit.
  Shrink the window while the number of distinct types of fruit is greater than 2.
'''

def fruits_into_baskets(fruits):
  window_start = max_length = 0
  fruit_frequency = {}

  # Try to extend the range [window_start, window_end].
  for window_end in range(len(fruits)):
    right_fruit = fruits[window_end]
    if right_fruit not in fruit_frequency:
      fruit_frequency[right_fruit] = 0
    fruit_frequency[right_fruit] += 1

    # Shrink the sliding window, until we are left with `2` fruits in the fruit frequency dictionary.
    while len(fruit_frequency) > 2:
      left_fruit = fruits[window_start]
      fruit_frequency[left_fruit] -= 1
      if fruit_frequency[left_fruit] == 0:
        del fruit_frequency[left_fruit]
      window_start += 1  # Shrink the window.
    max_length = max(max_length, window_end - window_start + 1)
  return max_length


def main():
  print('Expected output: 3')
  print("Actual output: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
  print('=====================')
  print('Expected output: 5')
  print("Actual output: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()
