class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')  # Integer.MIN_VALUE equivalent
        current_sum = 0

        for num in nums:
            current_sum += num

            # If the current sum is greater than the max sum then update the max sum's value to the current sum's value
            if current_sum > max_sum:
                max_sum = current_sum

            # If the current sum is 0, then it won't give any positive result, so it's better to start fresh by setting it to 0.
            if current_sum < 0:
                current_sum = 0

        return max_sum