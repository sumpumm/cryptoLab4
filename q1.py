import os
import math


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_primitive_roots(n):
    if not is_prime(n):
        return []

    phi = n - 1
    factors = set()
    i = 2
    while i * i <= phi:
        if phi % i == 0:
            factors.add(i)
            while phi % i == 0:
                phi //= i
        i += 1
    if phi > 1:
        factors.add(phi)

    primitive_roots = []
    for r in range(2, n):
        flag = False
        for factor in factors:
            if pow(r, (n - 1) // factor, n) == 1:
                flag = True
                break
        if not flag:
            primitive_roots.append(r)
    
    return primitive_roots

def main():
    try:
        num = int(input("Enter a number: "))

   
        if 1000 <= num <= 2000:
            print("Shutting down the system...")
           
            return
 
        if is_prime(num):
            roots = find_primitive_roots(num)
            if roots:
                print(f"Primitive roots of {num}: {roots}")
            else:
                print(f"No primitive roots found for {num}.")
        else:
            print(f"{num} is not a prime number.")
    
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
