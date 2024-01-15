def reve(n):
    temp=0
    while n!=0:
        r=n%10
        temp=(temp*10)+r
        n=n/10
    return temp

def square(n):
    return n*n

def factors(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    return sum

def cube_digits(n):
    c=0
    while n != 0:
        re=n%10
        c=c+(r*r*r)
        n=n/10
    return c

n=int(input())
squr=square(n)
rev=reve(n)
rev_sqr=square(rev)
rev_sqr_rev=reve(rev_sqr)
r=factors(n)
a=cube_digits(n)
if squr==rev_sqr_rev:
    print("Adam number")
else:
    print("Not a Adam number")
if r==n:
    print("Perfect number")
elif r>n:
    print("Abundant number")
elif r<n:
    print("Dificient number")
else:
    print("Invalid number")
if a==n:
    print("Armstrong number")
else:
    print("Not a Armstrong number")
    

