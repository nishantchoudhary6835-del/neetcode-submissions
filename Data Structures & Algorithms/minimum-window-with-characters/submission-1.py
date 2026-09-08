class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        countT = {}

        for c in t:
            countT[c] = countT.get(c, 0) + 1

        window = {}

        have = 0
        need = len(countT)

        res = [-1, -1]
        resLen = float("inf")

        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            # Check if this character's required frequency is satisfied
            if c in countT and window[c] == countT[c]:
                have += 1

            # Shrink the window while it remains valid
            while have == need:

                # Update minimum window
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # Remove left character
                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1

        l, r = res

        return s[l:r + 1] if resLen != float("inf") else ""