class Solution:
    def translate(self, c: str) -> int:
        mapping = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        return mapping.get(c, 0)  # Default to 0 for invalid characters

    def romanToInt(self, s: str) -> int:
        sum = 0
        cur = self.translate(s[0])

        for i in range(1, len(s)):
            next_val = self.translate(s[i])

            if cur < next_val:
                sum -= cur
            else:
                sum += cur

            cur = next_val  # Update cur for the next iteration

        return sum + cur  # Add the last numeral