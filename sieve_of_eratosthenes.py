def sieve_of_eratosthenes(n):
    """
    Returns a list of all prime numbers up to n (inclusive) using the Sieve of Eratosthenes algorithm.
    """
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

if __name__ == "__main__":
    N = int(input("Enter the value of N: "))
    primes = sieve_of_eratosthenes(N)
    print(f"Prime numbers up to {N}:")
    print(primes)
