use std::io::{self, BufRead};

fn difference_of_squares(n: i64) -> i64 {
    let sum_of_squares = n * (n + 1) * (2 * n + 1) / 6;
    let square_of_sum = ((n * (n + 1)) / 2).pow(2);
    square_of_sum - sum_of_squares
}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();
    let t = stdin_iterator
        .next()
        .unwrap()
        .unwrap()
        .trim()
        .parse::<i32>()
        .unwrap();

    for _ in 0..t {
        let n = stdin_iterator
            .next()
            .unwrap()
            .unwrap()
            .trim()
            .parse::<i64>()
            .unwrap();
        let result = difference_of_squares(n);
        println!("{}", result);
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(difference_of_squares(1), 0);
    }

    #[test]
    fn test_5() {
        assert_eq!(difference_of_squares(5), 170);
    }

    #[test]
    fn test_100() {
        assert_eq!(difference_of_squares(100), 25164150);
    }
}
