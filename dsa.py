# 1. Finding prime numbers

def factors(n):
    factorslist = []
    for i in range(1,n+1):
        if n%i == 0:
            factorslist.append(i)
    return(factorslist)

def prime(n):
    return(len(factors(n))==2)  #This is definition of a prime number that it exactly has 2 factors

primelist = []
for i in range(1,101):  #Finding prime numbers from 1 to 100
    if prime(i):
        primelist.append(i)
print(primelist)
print(len(primelist))

print(prime(87)) #Checking if a number is prime or not
print(prime(89)) #Checking if a number is prime or not

# 2. Finding GCD (Greatest Common Divisor) or HCF (Highest Common Factor) between two numbers:

#GCD always exists, GCD(m,n) <= min(m, n)
#So we will find the common factors from 1 to min(m,n) and then return the last such factor which will be our GCD or HCF.

def GCD(m,n):
    commonfactors = []
    k = min(m,n)
    for i in range (1,k+1):
        if m%i == 0 and n%i == 0:
            commonfactors.append(i)
    return(commonfactors[-1])

print(GCD(56,348))
print(GCD(2,3)) 

# Alternate way of finding GCD becuse we need the greatest common divisor not the whole list of common divisors.
# Here we can also eliminate the list and keep track of most recent common factor(mrcf)

def GCD(m,n):
    k = min(m,n)
    for i in range(1,k+1):
        if m%i == 0 and n%i == 0:
            mrcf = i   # Here we don't need to initialize mrcf as we know common factor 1 will always exist
    return(mrcf)  

print(GCD(56,348))
print(GCD(2,3)) 

# 3. Checking Primality

# Prime number n have exactly two factors (1, n), 1 is NOT a prime number

def prime(n):
    listfactors = []
    for i in range(1,n+1):
        if n%i == 0:
            listfactors.append(i)
    if len(listfactors) == 2:
        return(f"{n} is a prime number")
    else:
        return(f"{n} is not a prime number")  # Here I have used f-string
    
print(prime(3))
print(prime(2))
print(prime(4))

# More efficient way of finding out if a number is a prime number or not:
# if a number n is divisible by some number i then it is also divisible by n//i.
# Hence n//i is also a factor. They always come in pairs
# Why do we only check up to sqrt n ? Because after sqrt n, the partner factor has already appeared.
def primee(n):
    factlist = []
    i = 1 
    while i * i <= n:
        if n%i == 0:
            factlist.append(i)
            if i != n//i:
                factlist.append(n//i)
        i += 1

    if len(factlist) == 2:
        return(f"{n} is a prime number")
    else:
        return(f"{n} is not a prime number")
    
print(primee(3))
print(primee(2))
print(primee(4))

# 4. List the first m primes:

def primeee(n):
    factlist = []
    i = 1 
    while i * i <= n:
        if n%i == 0:
            factlist.append(i)
            if i != n//i:
                factlist.append(n//i)
        i += 1

    if len(factlist) == 2:
        return(True)
    else:
        return(False)
    
def firstmprimes(m):
    k = 1
    i = 1
    pl = []
  
    while k<=m:
        if primeee(i):
            pl.append(i)
            k += 1
        i+=1

    return(pl)

print(firstmprimes(2))
print(firstmprimes(25))

# 5. Another way of checking if the number is prime or not.
# We can do that by checking if there exist any factor between 2 and n-1.

def primeeee(n):
    result = True
    for i in range(2,n):
        if n % i ==0:
            result = False
            break
    return(result)

print(primeeee(2))
print(primeeee(28))

# We don't need to check the remaining factors. As soon as we get one such i which divides n we can break the loop
# We should be careful while using this break command as it can be very confusing
# Hence we can also write this code using while loop 
# There are infinitely many prime numbers
# How are they distributed?
# Twin primes: p & p+2 e.g, 5 & 7 ; 17 & 19. Basically the difference between them is 2

# 6. a.Find all prime numbers up to n,
#    b.Compute the difference between each consecutive pair of primes,
#    c.Count how many times each difference occurs,
#    d.Return those counts in a dictionary.

def p(n):
    fl = []
    for i in range(1, n+1):
        if n%i == 0:
            fl.append(i)
    return(fl)

def pnn(n):
    return(len(p(n))==2)
   

def np(m):
    nps = []
    for i in range(1, m+1):
        if pnn(i):
            nps.append(i)
    return(nps)

print(np(100))

def pmd(n):
    lastnumber = 2
    pmdf = {}
    for i in range(3,n+1):
        if pnn(i):
            df = i - lastnumber
            lastnumber = i
            if df in pmdf.keys():
                pmdf[df]=+1
            else:
                pmdf[df]=1
    return(pmdf)

print(pmd(100))

# 7. Can we find the GCD in a better way?

def GCD(m,n):
    (a,b)=(max(m,n),min(m,n))
    if a%b == 0:
        return(b)
    else:
        return(GCD(b,a%b))
    
print(GCD(18,9))
print(GCD(2,3))
print(GCD(4,36))











    
    






