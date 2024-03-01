#This is my solution to the challendge
#Write a Python script to:
#Display all the prime numbers between 1 to 250.
#Store the results in a results.txt file.
#Test the script. Verify that it produced the expected results in the results.txt file.
#Save the script and make a note of its location (absolute path) for future reference.

import math

def verify_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True


def list_of_prime_numbers():
    list_of_numbers = []
    for number in range(2, 251):
        if verify_prime(number):
            list_of_numbers.append(number)
    print(list_of_numbers)
    with open(r'results.txt', 'w') as fp:
        for element in list_of_numbers:
            fp.write("%s " % element)

list_of_prime_numbers()
