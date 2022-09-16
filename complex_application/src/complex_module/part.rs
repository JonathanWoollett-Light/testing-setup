pub fn flip(x: i32) -> i32 {
    -x
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn flip_test() {
        assert_eq!(flip(2), -2);
    }
}
