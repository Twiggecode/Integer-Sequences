use std::io::stdin;

fn main() {
    let mut input = String::new();
    println!("Which prime would you like?");
    
    stdin().read_line(&mut input).expect("Failed to read line.");

    let input: u32 = input.trim().parse()
        .expect("Please type a number!");

    println!("The {}th prime number is: {}", input+1, nth(input));
}

pub fn nth(n: u32) -> u32 {
    // Set initial values
    let mut prime_count = 0;
    let mut prime = 2;
    let mut checked_value = 3;

    // Count the primes we found and return the nth one
    while prime_count != n {
        if is_prime(checked_value) {
            prime = checked_value;
            prime_count += 1;
        }

        checked_value += 2;
    }
    prime
}

fn is_prime(n: u32) -> bool {
    // Skip over trivial values
    if n == 2 {
        return true;
    }
    if n < 2 {
        return false;
    }

    // Check ever number up to the sqrt of n + 1, as that is the range where possible divisors lay
    // Also only check every second number starting from 3 to skip the even numbers
    for check in (3..(f64::from(n).sqrt() as u32) + 1).step_by(2) {
        if n % check == 0 {
            return false;
        }
    }

    // If there is no possible divisor, return true
    true
}
