
import re
from traceback import print_list, print_tb
from typing import List
from unittest import result

class Solution:
  # Naive solution:
    # def findAnagrams(self, s: str, p: str) -> List[int]:
    #   result = []
    #   p_sorted = sorted(p)
    #   for i in range(len(s)):
    #     if i + len(p) > len(s): # break if we are out of bounds
    #       break
    #     if sorted(s[i:i+len(p)]) == p_sorted: # here we are comparing the sorted version of the substring to the sorted version of the pattern
    #       result.append(i)
    #   return result


  # Optimized solution:

    def build_hashmap(self, s):
        hashmap = {}
        for letter in s:
            if letter not in hashmap:
                hashmap[letter] = 1
            else:
                hashmap[letter] += 1
        return hashmap

    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Time complexity: O(n * len(P)) ~= O(n).
        # Space complexity: O(len(s) + len(p)).

        m, n, res = len(s), len(p), []

        # Build hashmap of p.
        hashmapP = self.build_hashmap(p)

        for beg in range(m-n+1):
            if beg == 0:
                # Build hashmap of s.
                hashmapS = self.build_hashmap(s[:n])
            else:
                # In dynamic variant, Remove value at left side of window.
                hashmapS[s[beg-1]] -= 1

                # Take into account new right side of window.
                if s[beg+n-1] in hashmapS:
                    hashmapS[s[beg+n-1]] += 1
                else:
                    hashmapS[s[beg+n-1]] = 1

            # Compare the 2 hashmaps to know whether s and p are anagrams or not.
            tmp = 0
            for letter in hashmapP:
                # Count only letters who belong in both hashmaps.
                if letter in hashmapS and hashmapS[letter] == hashmapP[letter]:
                    tmp += hashmapS[letter]

            if tmp == sum(hashmapP.values()):
                res.append(beg)

        return res








res = Solution().findAnagrams("ababababab", "aab")

print(res)
