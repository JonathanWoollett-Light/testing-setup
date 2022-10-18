// At crate root we adjust clippy settings.
#![warn(clippy::pedantic)]

pub use library_one::div;

fn main() {
    println!("nothing");
}

/// Unit tests
#[cfg(test)]
mod tests {
    #[test]
    fn one() {
        assert_eq!(1, 1);
    }
}
