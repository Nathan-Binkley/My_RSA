#RSA Attempt
#Nathan Binkley
#Programmed on 5/12/2019
#Runs on Python 3.7-


from ecdsa.numbertheory import inverse_mod as modinv
import sys, os

##
# This is my mod inverse function
# I coded this before I figured I could just import someone else's
#    for accuracy and assuring it works
# Please forgive me
x
# @param a = number to find inverse of
# @param m = number to test up until value of
# @returns values are := 1 (mod m)
# @pre a is of type int, z is of type int
# @post inverse of a based off m
##

# def modinv(a, m):
#
#     for x in range(1,m):
#         if ((m*x+1) % a == 0):
#             return (m*x+1)//a
#
#     return 1

e = 65537 #"Standard"
try:
    p = input("Input a prime number ") #works on minimum combined total of 26
    q = input("Input a different prime number (minimum added value of 26 for letters in alphabet) ")
    p = int(p)
    q = int(q)
    if p + q < 26:
        raise BaseException
except:
    print("Try again, added input values below 26")
    sys.exit()
n = p * q # to be found if breaking
d = modinv(e, ((p-1)*(q-1))) #for some reason D is always 1 for any number combination
                            # that p + q < 26


plaintext = input("What would you like to encrypt? ")
plaintext = plaintext.lower()
print("Your plaintext is: " + plaintext)
print("p: " + str(p))
print("q: " + str(q))

plain_list_num = []
enc_list_num = []
end_list_num = []
ending = ""

for i in plaintext:
    plain_list_num.append(ord(i))
print("Your plaintext list is: " + str(plain_list_num))

for i in plain_list_num:
    enc_list_num.append(i**e % n)
print("Your encrypted values are " + str(enc_list_num))

for i in enc_list_num:
    end_list_num.append(i**d % n)

print("Your end result list is " + str(end_list_num))

for i in end_list_num:
    ending += chr(i)

print("Plaintext(Unencrypted) is: " + ending)
