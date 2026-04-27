class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = sorted(s)
        y = sorted(t)
        if d == y:
            return True
        else:
            return False