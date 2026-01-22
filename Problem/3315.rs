pub fn min_bitwise_array(nums: Vec<i32>) -> Vec<i32> {
        let mut ans : Vec<i32> = vec![];
        for mut x in &nums {
            let mut bit : i32 = 1;
            let mut res : i32 = -1;
            while ((x & bit) != 0) {
                res = x - bit;
                bit <<= 1;
            }
            ans.push(res);
        }

        return ans;
}