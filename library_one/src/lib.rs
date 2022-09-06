// At crate root we adjust clippy settings.
#![warn(clippy::pedantic)]

#[must_use]
pub fn div(a: i32, b: i32) -> i32 {
    a / b
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
