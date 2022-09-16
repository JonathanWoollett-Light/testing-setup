#[cfg(unix)]
const DEPS: [&str; 2] = ["gcc", "python3"];

#[cfg(unix)]
fn check(x: &str) {
    let output = std::process::Command::new("dpkg")
        .args(&["-l", x])
        .output()
        .unwrap();
    match output.status.code() {
        Some(0) => (),
        _ => panic!("Missing dependency: {}", x),
    }
}

fn main() {
    #[cfg(unix)]
    for dep in DEPS {
        check(dep);
    }
}
