class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set ()
        for n in range(len(nums)):
            if nums[n] in window:
                return True
            window.add(nums[n])
            if n >= k:
                window.remove(nums[n - k])
        return False
        