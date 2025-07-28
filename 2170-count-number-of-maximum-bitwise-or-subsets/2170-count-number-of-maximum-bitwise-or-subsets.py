from typing import List

class Solution:
  """
  Solves the problem of finding the number of subsets with the maximum bitwise OR.
  """
  def countMaxOrSubsets(self, nums: List[int]) -> int:
    """
    Calculates the maximum possible bitwise OR of a subset of nums and
    returns the number of different non-empty subsets with that maximum bitwise OR.

    The solution works in two main steps:
    1. It first determines the maximum possible bitwise OR value. This value is simply
       the bitwise OR of all elements in the input array, as the OR operation
       is monotonic (i.e., ORing with more numbers can only set more bits to 1,
       not 0).
    2. It then uses a recursive backtracking function to explore all possible
       subsets of `nums`. For each subset, it calculates its bitwise OR. If this
       value matches the maximum possible OR, a counter is incremented.

    The backtracking function `backtrack(index, current_or)` considers each element
    from `index` 0 to n-1. At each step, it branches into two possibilities:
    - Include the current element `nums[index]` in the subset.
    - Exclude the current element `nums[index]` from the subset.

    This process systematically generates all 2^n subsets. The base case for the
    recursion is when all elements have been considered (`index == n`). At this point,
    the final `current_or` of the generated subset is checked against `max_or`.

    Args:
      nums: A list of integers. The constraints are 1 <= nums.length <= 16
            and 1 <= nums[i] <= 10^5.

    Returns:
      The number of non-empty subsets that achieve the maximum bitwise OR.
    """
    # Step 1: Calculate the maximum possible bitwise OR.
    # The bitwise OR of any subset cannot exceed the bitwise OR of the entire array.
    max_or = 0
    for num in nums:
        max_or |= num

    # Initialize a counter for subsets that result in max_or.
    self.count = 0
    n = len(nums)

    # Step 2: Use a recursive backtracking approach to explore all subsets.
    def backtrack(index: int, current_or: int):
        """
        Recursively explores subsets starting from the given index.

        Args:
          index: The current index in the nums array to consider.
          current_or: The bitwise OR of the subset constructed so far.
        """
        # Base case: we have considered all elements.
        if index == n:
            # If the OR of the generated subset equals the maximum possible OR,
            # we have found a valid subset.
            if current_or == max_or:
                self.count += 1
            return

        # Recursive Step:
        # We have two choices for each element: either include it or not.

        # Choice 1: Include nums[index] in the current subset.
        # We update the current_or with the new element and move to the next index.
        backtrack(index + 1, current_or | nums[index])

        # Choice 2: Do not include nums[index] in the current subset.
        # The current_or remains the same, and we move to the next index.
        backtrack(index + 1, current_or)

    # Start the backtracking process from the first element (index 0)
    # with an initial bitwise OR of 0 (representing an empty set to start with).
    backtrack(0, 0)

    # The problem asks for non-empty subsets. The initial call `backtrack(0, 0)`
    # explores all 2^n subsets. The empty subset has a bitwise OR of 0.
    # Given the problem constraint `1 <= nums[i]`, the `max_or` will always be > 0.
    # Therefore, the empty subset's OR (0) will never equal `max_or`,
    # so it is never counted. The final count is implicitly correct for non-empty subsets.
    return self.count
