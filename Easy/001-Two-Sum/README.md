# Problem: Two Sum

## Problem Description

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

### Constraints

1. Each input has exactly one solution.
2. The same element cannot be used twice.

### Example

**Input**: `nums = [2,7,11,15], target = 9`
**Output**: `[0,1]`
**Explanation**: `nums[0] + nums[1] = 2 + 7 = 9`.

## Solution Explanation

The solution uses a hash map to efficiently find the pair of numbers that sum to the target. The hash map stores each number's value and index as it iterates through the array.

### Complexity

- **Time Complexity**: `O(n)` (single pass through the list)
- **Space Complexity**: `O(n)` (space for the hash map)

## Implementation

```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in h:
                return [h[diff], i]
            h[n] = i
```
