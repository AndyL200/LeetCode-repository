impl Solution {
    pub fn bitwise_complement(n: i32) -> i32 {
        if(n == 0) {return 1;}
        let q = -n - 1;
        let pos = 31 - n.leading_zeros();
        let r = 1 << pos;
        let g = (r << 1) - 1;
        return q & g;
    }
}

impl Solution {
    pub fn bitwise_complement(n: i32) -> i32 {
        if (n == 0) {return 1;}
        let pos : u8 = 31 - n.leading_zeros() as u8;
        let mask : i32 = (1 << (pos+1));
        return (mask-1) ^ n;
    }
}