from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = defaultdict(int)

        have = 0
        required = len(need)

        l = 0
        res = ""
        res_len = float("inf")

        for r in range(len(s)):
            c = s[r]
            window[c] += 1

            if c in need and window[c] == need[c]:
                have += 1

            while have == required:
                if (r - l + 1) < res_len:
                    res = s[l:r+1]
                    res_len = r - l + 1

                window[s[l]] -= 1

                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1

                l += 1

        return res

        