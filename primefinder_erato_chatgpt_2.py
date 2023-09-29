#!/user/bin/env python3

# Prímszám kereső Eratosztenész szitája alapján
# a kód alapja chatGPT-től származik
# chatGPT link: https://chat.openai.com/share/178e526e-d0bd-48b9-8e1a-8f47e035ed32

# ELLENŐRIZNI KELL ennek a változatnak a működését!

def eratosthenes_sieve(n):
    sieve = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
        p += 1
    primes = [p for p in range(2, n + 1) if sieve[p]]
    return primes

# Első tartomány: 2-től 1000-ig
n1 = 1000
primes1 = eratosthenes_sieve(n1)

# Második tartomány: 1001-től 2000-ig
n2 = 2000
# Most használjuk a korábbi prímeket az új tartomány szitájához
sieve = [True] * (n2 - n1 + 1)
for p in primes1:
    start = max(p * p, (n1 // p + 1) * p)
    for i in range(start, n2 + 1, p):
        sieve[i - n1] = False
primes2 = [n1 + i for i, is_prime in enumerate(sieve) if is_prime]
print(primes2)
