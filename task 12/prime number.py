print("\n  set 1")
a=set()
c=int(input("enter the count:"))
for i in range(c):
      e=int(input("enter the value"))
      a.add(e)
      print("the set 1:",a)

print("\n prime numbers")
primes=set()

for num in  a:
    if num > 1:
        for i in range(2, int(num**0.5)+1):
           if num % i== 0:
              break
else:
      primes.add(num)
print("Prime numbers in the set:", primes)
        
