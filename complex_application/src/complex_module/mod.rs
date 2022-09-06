mod part;
use part::flip;
pub fn sub_flip(a: i32, b: i32) -> i32 {
    a - flip(b)
}
