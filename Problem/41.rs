use std::collections::HashSet;
impl Solution {
    pub fn first_missing_positive(nums: Vec<i32>) -> i32 {
        let mut seen : Vec<bool> = vec![false; nums.len()+1];
        let l = nums.len();
        for n in nums {
            let n = n as usize;
            if (n > 0 && n <= l) {
                seen[n] = true;
            }
        }
        for i in 1..=l {
            if (!seen[i]) {
                return i as i32;
            }
        }
        return (l + 1) as i32;  
    }
}