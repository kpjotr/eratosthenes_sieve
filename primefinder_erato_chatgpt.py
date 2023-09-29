#!/usr/bin/env python3

# Prímszám kereső Eratosztenész szitája alapján
# a kód alapja chatGPT-től származik
# chatGPT link: https://chat.openai.com/share/178e526e-d0bd-48b9-8e1a-8f47e035ed32
# ez a változat hibásan működik, mivel minden tartományban 2-től keresi a prímeket

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


n2 = int(input("Add meg a felső limitet  (legyen 1000-el osztható)! "))
# Első tartomány: 2-től 1000-ig
n1 = int(n2 / 2)
primes1 = eratosthenes_sieve(n1)

# Második tartomány: 1001-től 2000-ig
primes2 = eratosthenes_sieve(n2)
primes2 = [p for p in primes2 if p >= n1 + 1]  # Szűrjük csak az 1001 és 2000 közötti prímekre

# print(primes1)
# print()
# print(primes2)
# print()
print("primes1 lenght: ", len(primes1))
print("primes2 lenght: ", len(primes2))
print("sum lenght: ", (len(primes1) + len(primes2)))
print("last prime: ", primes2[-1])
