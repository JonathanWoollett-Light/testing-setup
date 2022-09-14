fn main() {
    println!("cargo:rerun-if-changed=./setup.py");
    // Run setup script
    let output = std::process::Command::new("gnome-terminal")
        .args(&["--wait", "--", "python3", "setup.py"])
        .output()
        .unwrap();
    // Assert script succeeded
    assert_eq!(output.status.code(), Some(0));
}
