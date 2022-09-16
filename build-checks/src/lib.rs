use std::str::FromStr;

macro_rules! cargo_process {
    ($($arg:literal),*) => {{
        std::process::Command::new("cargo")$(.arg($arg))*.output().unwrap();
    }}
}

pub fn check(name: &str) {
    let audit = bool::from_str(env!("AUDIT")).unwrap();
    if audit {
        cargo_process!("audit");
    }

    let fmt = env!("FMT");
    match fmt {
        "fix" => cargo_process!("fmt"),
        "check" => cargo_process!("fmt","--check"),
        _ => unreachable!()
    }

    let clippy = env!("CLIPPY");
    match clippy {
        "allow" => (),
        "warn" => cargo_process!("clippy"),
        "deny" => cargo_process!("clippy","--","--deny","warnings"),
        "fix" => cargo_process!("clippy","--fix"),
        _ => unreachable!()
    }
    let size = bool::from_str(env!("SIZE")).unwrap();
    if size {
        
    }
}