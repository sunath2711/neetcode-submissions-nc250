# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            # Avoid potential integer overflow
            mid = left + (right - left) // 2
            res = guess(mid)

            if res == 0:
                return mid  # Picked number found!
            elif res == -1:
                right = mid - 1  # Picked number is lower
            else:
                left = mid + 1  # Picked number is higher

        return -1
        