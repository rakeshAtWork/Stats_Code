# Input any Roman Number 
# Output we can aspect the value to the code given.

class Solution:
    def romanToInt(self, s: str) -> int:
        mp = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i] == 'I' and s[i + 1] == 'V':
                ans += 4
                i += 2
            elif i + 1 < len(s) and s[i] == 'I' and s[i + 1] == 'X':
                ans += 9
                i += 2
            elif i + 1 < len(s) and s[i] == 'X' and s[i + 1] == 'L':
                ans += 40
                i += 2
            elif i + 1 < len(s) and s[i] == 'X' and s[i + 1] == 'C':
                ans += 90
                i += 2
            elif i + 1 < len(s) and s[i] == 'C' and s[i + 1] == 'D':
                ans += 400
                i += 2
            elif i + 1 < len(s) and s[i] == 'C' and s[i + 1] == 'M':
                ans += 900
                i += 2
            else:
                ans += mp[s[i]]
                i += 1
        return ans

# Example usage:
s1 = Solution()
ans = s1.romanToInt("XC")
print("The output is :", ans)

