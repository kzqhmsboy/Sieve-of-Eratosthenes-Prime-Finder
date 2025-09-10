# Sieve of Eratosthenes Prime Finder

This Python script finds all prime numbers up to a given number N using the efficient Sieve of Eratosthenes algorithm.

## Usage

1. Make sure you have Python installed (version 3.x recommended).
2. Download or copy the file `sieve_of_eratosthenes.py`.
3. Run the script from your terminal:

```bash
python sieve_of_eratosthenes.py
```

4. When prompted, enter the value of N (the upper limit to search for primes).

The script will output all prime numbers up to and including N.

## Example

```
Enter the value of N: 30
Prime numbers up to 30:
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

## How it Works

- The algorithm initializes a boolean list up to N.
- It iteratively marks the multiples of each prime number as non-prime.
- The remaining unmarked numbers are the primes.

## License

This project is open source and available under the MIT License.
