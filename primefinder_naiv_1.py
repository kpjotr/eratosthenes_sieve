#!/user/bin/env python3

# prime number finder
# ---------------

import time

# defining global variables
primes = [2, 3]  # fill the 'primes' list with the first two prime number
# (the 0 and 1 isn't primes -> https://en.wikipedia.org/wiki/Prime_number)
inspected_numb = 5  # counter of inspected numbers, start from 5
counter = 0  # for counting the number of checked numbers
TimeToPrint = 0  # for timing to print some info to console

print()  # make an empty line on console

starttime = (time.time())  # set the starting time of the main loop (because wanna measure the elapsed time)

while True:  # endless cicle for main iteration
    try:
        not_prime = False  # set variable to false
        counter += 1  # count the number of checked numbers
        for i in primes:  # iterate on elements of variable 'primes'
            # we only checking numbers as long as the prime is less than the square root of the checked number
            if i <= inspected_numb ** (1 / 2):
                # if the examined number is divisible by a previous prime without a remainder, then it is not prime
                if (inspected_numb % i) == 0:
                    not_prime = True  # set the variable true, if the checked number isn't prime
                    break  # exit from for loop

        if not_prime == False:
            primes.append(inspected_numb)  # append to list of primes the found prime
            if TimeToPrint < time.time() and time.time() > starttime + 1:
                endtime = time.time()
                text = "Checked numbers: " + str(counter) + " | Last found prime: " + str(
                    inspected_numb) + " | Sum primes: " + str(len(primes)) + " | Elapsed time: " + str(
                    int((endtime - starttime))) + " sec | Prime/Sec: " + str(int(len(primes) / (endtime - starttime)))
                print(f'\r {text}', end='')
                TimeToPrint = time.time() + 2
        inspected_numb += 2  # increment + 2, because want to check only odd numbers
    except KeyboardInterrupt:
        print("\nThe program is terminated manually")
        raise SystemExit

# for i in primes:
#    print(i, end =", ")
# endtime = (time.time())
# print("\n\nStart timestamp:", starttime, "\nEnd timestamp:", endtime, "\nElapsed time:", (endtime-starttime), "\nPrime/Sec:", (len(primes)/(endtime-starttime)))
