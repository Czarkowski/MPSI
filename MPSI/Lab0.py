import math
import random

#1
K =  8.988e9
print(f"K = {K:.3f} N*m2/C2")   

#2
print(f"Sqtr = {math.sqrt(K):.4f}")   

#3
a = 32
b = 11
print(a//b)

#4
a = 31
b = 9
print(a%b)

#5
imie = input("imie: ")
nazwisko = input("nazwisko: ")
wiek = int(input("wiek: "))
cenaCebuli = float(input("Cena Cebuli: "))
print(f"imie: {imie}, nazwisko: {nazwisko}, wiek: {wiek}, Cena Cebuli: {cenaCebuli}")

#6
for i in range(7):
    print(random.randint(2,89))

