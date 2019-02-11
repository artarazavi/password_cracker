# ==========================================================================================
# Crated by Seyedeh Arta Razavi
# For class CS590A

from passlib.hash import lmhash
from itertools import permutations
import itertools
import string

# ==========================================================================================
# Main method

# gather options from user input
password = input("input password to guess: ")
attack_mode = input("pick attack mode dictionary or brute_force: ")
min = 0
max = 0
# if attack mode is dictionary user must supply dictionary
if attack_mode == "dictionary":
    file_path = input(
        "enter file path to dictionary where list is contained: ")
# if attack mode is brute force user must supply min and max password length
if attack_mode == "brute_force":
    crunch = input(
        "enter crunch mode [yes/no] (user input possible chracters) ")
    # if crunch mode chosen the user inputs the chars for program to permutate
    if crunch == "yes":
        user_crunch = input("input crunch string to permutate into password ")
    min = input("input min password length: ")
    max = input("input max password length: ")

h = lmhash.hash(password)

print("the password's hash is: ")
print(h)

if attack_mode == "brute_force":
    # all possible permutations of these chracaters will be tested
    if crunch == "yes":
        asciichars = user_crunch
    else:
        asciichars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    tries = 0
    # create permutations of length min to max
    for length in range(int(min), (int(max)+1)):
        # create permutations with set of chracters specified with specified length
        # repeat option allows permutations with repeating characters
        for pass_guess in itertools.product(asciichars, repeat=length):
            tries = tries + 1
            # password guessed is a list must be joined with an empty string to become string
            pass_guess = "".join(pass_guess)
            try:
                # hash guessed password
                pass_hash = lmhash.hash(pass_guess)
                if pass_hash == h:
                    # if password is found print to console and exit program
                    print("password is: ")
                    print(pass_guess)
                    print("guessed in " + str(tries) + " tries.")
                    break
            except Exception:
                pass

if attack_mode == "dictionary":
    # read in lines from dictionary file
    lines = [line.rstrip('\n') for line in open(file_path)]
    tries = 0
    for line in lines:
        tries = tries + 1
        try:
            if lmhash.verify(line, h):
                # if password is found print to console and exit program
                print("password is: ")
                print(line)
                print("guessed in " + str(tries) + " tries.")
                break
        except Exception:
            pass
