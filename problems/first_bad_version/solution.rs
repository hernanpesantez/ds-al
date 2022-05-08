impl Solution {
  pub fn first_bad_version(&self, n: i32) -> i32 {
    let mut l = 1;
    let mut r = n;
    while l < r {
      let m = l + (r - l) / 2;
      if self.is_bad_version(m) {
        r = m;
      } else {
        l = m + 1;
      }
    }
    l as i32 // this line returns the first bad version
  }
}
