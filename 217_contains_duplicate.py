class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # the idea here is to create a set and return true if there is any occurence already present in the set else false
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False