
def perfect():
    print("--Perfect Number Check--") 
    n1 = []
    a = int(input("Enter the count of values: "))

    for i in range(a):
        val = int(input("Enter value: "))
        n1.append(val)

    print("List of values:", n1)

    for num in n1:
        divisors = [i for i in range(1, num) if num % i == 0]
        if sum(divisors) == num:
            print(num, "is a Perfect Number")
        else:
            print(num, "is NOT a Perfect Number")


if __name__ == "__main__":
    perfect()

