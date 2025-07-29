from typing import List

class Solution:
  """
  Solves the problem of finding the smallest subarray with the maximum bitwise OR
  for each starting index.
  """
  def smallestSubarrays(self, nums: List[int]) -> List[int]:
    """
    For each index i, finds the length of the minimum sized non-empty subarray
    starting at i that has the maximum possible bitwise OR.

    The solution iterates from the end of the array to the beginning. The core
    idea is to keep track of the closest future index where each bit is set.

    Let's define `last[b]` as the index of the most recent occurrence of a number
    with the b-th bit set, as we scan from right to left.

    When we are at index `i`, the maximum possible bitwise OR for any subarray
    starting at `i` is determined by the bits available in the suffix `nums[i:]`.
    To achieve this maximum OR in the shortest possible subarray `nums[i...j]`,
    the endpoint `j` must be the farthest index we need to reach to collect all
    the necessary bits. This farthest index `j` is the maximum of `last[b]`
    for all bits `b` that are present in the suffix `nums[i:]`.

    The algorithm proceeds as follows:
    1. Initialize an array `last` of size 30 (since nums[i] < 2^30) to store
       the most recent index for each bit. Initialize all to -1 (or any
       indicator that the bit has not been seen).
    2. Iterate from `i = n-1` down to `0`.
    3. For each `i`, first update the `last` array with the bits from `nums[i]`.
       If the b-th bit is set in `nums[i]`, then `last[b]` becomes `i`.
    4. Then, calculate the required endpoint `j` (farthest_reach). This is the
       maximum value in the `last` array, considering only the bits that have
       actually been seen so far (i.e., where `last[b]` is a valid index).
    5. The length of the subarray is `farthest_reach - i + 1`. Store this.

    This approach has a time complexity of O(n * log(max(nums))) and a space
    complexity of O(log(max(nums))), making it efficient for the given constraints.

    Args:
      nums: A list of non-negative integers.

    Returns:
      A list of integers where the i-th element is the length of the smallest
      subarray starting at i with the maximum bitwise OR.
    """
    n = len(nums)
    ans = [0] * n
    
    # `last[b]` stores the index of the most recent number with bit `b` set.
    # Initialize with -1 to indicate that no bit has been seen yet.
    last = [-1] * 30

    # Iterate from right to left.
    for i in range(n - 1, -1, -1):
        # Update `last` with the bits from the current number.
        for b in range(30):
            if (nums[i] >> b) & 1:
                last[b] = i

        # The end of the smallest subarray starting at `i` is determined by the
        # farthest "last seen" index of any bit that is available in the suffix.
        farthest_reach = i
        for b in range(30):
            # We only consider bits that have been seen so far (last[b] != -1).
            # The subarray must extend to include the last occurrence of each of these bits.
            if last[b] != -1:
                farthest_reach = max(farthest_reach, last[b])
        
        # The length of this subarray is the distance from i to the farthest reach.
        ans[i] = farthest_reach - i + 1
        
    return ans
