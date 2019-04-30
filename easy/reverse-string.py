from typing import List


# Problem 344: Reverse string (done recursively as part of recursion lesson)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        def helper(index: int, s: List[str]):
            if index >= len(s) / 2:
                return

            helper(index + 1, s)
            s[index], s[len(s) - index - 1] = s[len(s) - index - 1], s[index]

        helper(0, s)
