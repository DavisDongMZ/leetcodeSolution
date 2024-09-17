class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        left_max = height[left]
        right_max = height[right]

        water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]

            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]

        return water


# initialize two ptrs, moving from left and right to middle
# if left max < right max move left to middle otherwise right
# each time ptr moves, keep track of the heightest of left and right
# get water by heightest - current
