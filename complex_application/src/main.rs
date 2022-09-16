// At crate root we adjust clippy settings.
#![warn(clippy::pedantic, clippy::restriction)]
#![allow(clippy::blanket_clippy_restriction_lints)]

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
    println!("done {}", c);
    println!("true = {}", its_true());

    unsafe {
        println!("something boring");
    }
    println!("{}",fibonacci_recursive(13));
}

pub fn fibonacci_recursive(_n: i32) -> u64 {
	if _n < 0 {
		panic!("{} is negative!", _n);
	}
	match _n {
		0     => panic!("zero is not a right argument to fibonacci_recursive()!"),
		1 | 2 => 1,
		3     => 2,
		/*
		50    => 12586269025,
		*/
		_     => fibonacci_recursive(_n - 1) + fibonacci_recursive(_n - 2)
	}
}

pub fn fibonacci(n: i32) -> u64 {
	if n < 0 {
		panic!("{} is negative!", n);
	} else if n == 0 {
		panic!("zero is not a right argument to fibonacci()!");
	} else if n == 1 {
		return 1;
	}
    let a = 2;
	let mut sum = 0;
	let mut last = 0;
	let mut cur = 1;
    let b = a + 4;
	for _i in 1..n {
		sum = last + cur;
		last = cur;
		cur = sum;
	}
	sum
}

fn add(a: i32, b: i32) -> i32 {
    a + b
}

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
        assert_eq!(its_true(), true);
    }
}
