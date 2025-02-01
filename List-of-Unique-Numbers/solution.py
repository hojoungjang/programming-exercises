"""
백준
List of unique numbers
https://www.acmicpc.net/problem/13144

Use two pointers.
Let's name the pointers `start` and `end` and
both start at 0.

If the elements that fall between (inclusive) the
two pointers are unique we continue expanding `end`
At any point there are duplicate elements, start
moving `start` pointer to the right.

When updating `start`, also remove the set of numbers 
that fall  between the two pointers and the number of
subarrays that start at `start` pointer and has unique
elements. This should be the length of the window 
(before adding the new element). Do the counting and
see for yourself. 

For example, the array is like this `s` and `e` mark the pointers.
[1, 1, 2, 3, 7, 2, 5]
       s     e
The possible subarrays with length greater than or equal to one and
that starts at `s` and contain unique elements are
[2], [2,3], [2,3,7] which is equal to 3.

Lastly, don't forget to account for the case where there are 
no duplicate number found in the above process. In this case,
the count is not updated. Remeber, we only update count when
we encounter a duplicate so if we don't, the window keeps 
growing and we just end without updating the count. 

To account for these numbers, we iterate from `start` to end of 
the array and again add the window size of each of them.
"""
import sys

def solution(nums: list[int]) -> int:
    start = 0
    seen = set()
    count = 0

    for end in range(len(nums)):
        while nums[end] in seen and start < end:
            seen.remove(nums[start])
            count += end - start
            start += 1
        seen.add(nums[end])
    
    for idx in range(start, len(nums)):
        count += len(nums) - idx

    return count

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    nums = [int(num) for num in sys.stdin.readline().strip().split()]
    print(solution(nums))