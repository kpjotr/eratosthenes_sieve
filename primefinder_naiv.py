# eddig ez a leggyorsabb limitless teszt

import time

def isPrime(n):
    if n <= 1:
        return False
    else:
        if n % 2 == 0 or n % 3 == 0:
            return False
    i = 5
    while (i*i <= n):
        if n % i == 0 or  n % (i + 2) == 0:
            return False
        i = i + 6
    return True

primes = [2,3]
lastlen = len(primes)
c=3
delay = 10
printtime = 0
while True:
    if isPrime(c):
        primes.append(c)
        if printtime < time.time():
            primesNr = len(primes)
            speed = (primesNr - lastlen) / (delay/2)
            print(f'\r{c} : {primesNr} : {speed}', end='')
            printtime = time.time() + delay
            lastlen = len(primes)
    c += 2

print("\n\nprimes lenght: ", len(primes))
print("first prime: ", primes[0])
print("last prime: ", primes[-1])