// At crate root we adjust clippy settings.
#![warn(clippy::pedantic)]

#[must_use]
pub fn div(a: u32, b: u32) -> u32 {
    a / b
}

#[must_use]
pub fn plus(x: i32) -> i32 {
    x + 1
}

/// Units tests
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn one() {
        assert_eq!(div(4, 1), 4);
    }
    #[test]
    fn two() {
        assert_eq!(div(4, 2), 2);
    }
    #[test]
    fn three() {
        assert_eq!(div(4, 3), 1);
    }
}
