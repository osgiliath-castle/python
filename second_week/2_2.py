""" function calculates largest prime factor """
def maximum_prime(n):
    min_prime = 2
    while min_prime * min_prime <= n:
        if n % min_prime:
            min_prime += 1
        else:
            n //= min_prime
    return n
    
