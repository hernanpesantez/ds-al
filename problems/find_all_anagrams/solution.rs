// # Optimized solution:

// def build_hashmap(self, s):
//     hashmap = {}
//     for letter in s:
//         if letter not in hashmap:
//             hashmap[letter] = 1
//         else:
//             hashmap[letter] += 1
//     return hashmap

// def findAnagrams(self, s: str, p: str) -> List[int]:
//     # Time complexity: O(n * len(P)) ~= O(n).
//     # Space complexity: O(len(s) + len(p)).

//     m, n, res = len(s), len(p), []

//     # Build hashmap of p.
//     hashmapP = self.build_hashmap(p)

//     for beg in range(m-n+1):
//         if beg == 0:
//             # Build hashmap of s.
//             hashmapS = self.build_hashmap(s[:n])
//         else:
//             # In dynamic variant, Remove value at left side of window.
//             hashmapS[s[beg-1]] -= 1

//             # Take into account new right side of window.
//             if s[beg+n-1] in hashmapS:
//                 hashmapS[s[beg+n-1]] += 1
//             else:
//                 hashmapS[s[beg+n-1]] = 1

//         # Compare the 2 hashmaps to know whether s and p are anagrams or not.
//         tmp = 0
//         for letter in hashmapP:
//             # Count only letters who belong in both hashmaps.
//             if letter in hashmapS and hashmapS[letter] == hashmapP[letter]:
//                 tmp += hashmapS[letter]

//         if tmp == sum(hashmapP.values()):
//             res.append(beg)

//     return res


use std::collections::HashMap;

impl Solution {

  fn man

  pub fn find_anagrams(s: String, p: String) -> Vec<i32> {
    let mut res = vec![];
    let mut hashmapP = HashMap::new();
    let mut hashmapS = HashMap::new();
    let mut n = p.len();
    let mut m = s.len();
    let mut i = 0;
    let mut j = 0;
    let mut tmp = 0;

    for c in p.chars() {
      hashmapP.insert(c, hashmapP.get(&c).unwrap_or(&0) + 1);
    }

    while i < m && j < n {
      if j == 0 {
        hashmapS.insert(s.chars().nth(i).unwrap(), hashmapS.get(&s.chars().nth(i).unwrap()).unwrap_or(&0) + 1);
      } else {
        hashmapS.insert(s.chars().nth(i).unwrap(), hashmapS.get(&s.chars().nth(i).unwrap()).unwrap_or(&0) + 1);
        hashmapS.insert(s.chars().nth(i-1).unwrap(), hashmapS.get(&s.chars().nth(i-1).unwrap()).unwrap_or(&0) - 1);
      }

      if hashmapS.get(&s.chars().nth(i).unwrap()).unwrap() == hashmapP.get(&s.chars().nth(i).unwrap()).unwrap() {
        tmp += 1;
      }

      if tmp == hashmapP.len() {
        res.push(i - n + 1);
      }

      i += 1;
      j += 1;
    }

    res.to_vec()
  }
}
