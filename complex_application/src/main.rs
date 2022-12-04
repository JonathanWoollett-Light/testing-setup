// At crate root we adjust clippy settings.
#![warn(clippy::pedantic)]

pub use library_one::div;

mod complex_module;
mod simple_module;
use complex_module::sub_flip;
use simple_module::its_true;

// Pull `TryFrom` into scope so can use `u8::try_from`.
use std::convert::TryFrom;

fn main() {
    println!("Hello, world!");
    let x = 2;
    let y = 3;
    let a = add(x, y);

    let _b = sub_flip(x, y);
    let c: u8 = u8::try_from(a).unwrap();
    println!("done {c}");
    println!("true = {}", its_true());

    println!("something boring");
}

fn add(a: i32, b: i32) -> i32 {
    a + b
}
// Small doc change.
/// Unit tests
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn add_test_1() {
        assert_eq!(add(1, 2), 3);
    }
    #[test]
    fn add_test_2() {
        assert_eq!(add(2, 3), 5);
    }
    #[test]
    fn add_test_3() {
        assert_eq!(add(3, 4), 7);
    }
    #[test]
    fn dumb() {
        assert!(its_true());
    }
    #[allow(clippy::nonminimal_bool)]
    #[test]
    fn some_dumber() {
        assert!(!!its_true());
    }
}
