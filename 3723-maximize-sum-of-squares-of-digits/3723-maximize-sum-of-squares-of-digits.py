class Solution(object):
    def maxSumOfSquares(self, num, total_sum):
        if total_sum > 9*num:
            return ""
        nines = total_sum // 9
        remainder = total_sum % 9

        zeros = num - nines - (1 if remainder > 0 else 0)

        result = "9" * nines
        if remainder > 0:
            result += str(remainder)
        result += "0" * zeros

        return result