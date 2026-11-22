class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): return False

        const_s = {}
        const_t = {}

        for i in range(len(s)):
            const_s[s[i]] = const_s.get(s[i], 0) + 1
            const_t[t[i]] = const_t.get(t[i], 0) + 1

        return const_s == const_t