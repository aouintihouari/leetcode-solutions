from typing import List

class Solution:
    """
    LeetCode Problem: Two Sum

    Description:
    Given an array of integers `nums` and an integer `target`, return the indices
    of the two numbers such that they add up to `target`.

    Note:
    - Each input has exactly one solution.
    - The same element cannot be used twice.

    Approach:
    - Use a hash map (dictionary) to store the values and their indices.
    - For each number in the array, calculate the difference (`target - number`).
    - If the difference exists in the hash map, return the indices of the current number and the difference.
    - Otherwise, add the number and its index to the hash map.
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store numbers and their indices
        h = {}
        for i, n in enumerate(nums):
            # Calculate the difference needed to reach the target
            diff = target - n
            if diff in h:
                # If the difference is found, return indices
                return [h[diff], i]
            # Otherwise, store the current number and its index
            h[n] = i
