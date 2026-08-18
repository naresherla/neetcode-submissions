class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = {}
        for v in s:
            seen[v] = seen.get(v,0)+1
        for k in t:
            if k not in seen:
                return False
            seen[k] -= 1
            if seen[k] < 0:
                return False
        return True
