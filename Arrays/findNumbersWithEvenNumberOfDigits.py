class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0
        for num in nums:
            if self.hasEvenDigits(num):
                count += 1
        return count

    def hasEvenDigits(self, num: int) -> bool:
        digit_count = 0
        while num > 0:
            num //= 10  # Integer division to remove the last digit
            digit_count += 1
        return digit_count % 2 == 0