const DEPS: [&str; 2] = ["gcc", "python3"];

fn check(x: &str) {
    let output = std::process::Command::new("dpkg")
        .args(&["-l", x])
        .output()
        .unwrap();
    match output.status.code() {
        Some(0) => (),
        _ => panic!("Missing depdendency: {}", x),
    }
}

fn main() {
    for dep in DEPS {
        check(dep);
    }
}
