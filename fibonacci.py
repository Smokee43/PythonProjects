nterms = int(input("How many terms? "))

#first tow terms
n1, n2 = 0, 1
count = 0

#check if the number of terms is valid
if (nterms <= 0):
    print("Enter a positive integer: ")
elif (nterms == 1):
    print("Fibonacci sequence upto", nterms, ":")
    print(n1)
else:
    print("Fibonacci sequece:")
    while( count < nterms):
        print(n1)
        nth = n1 + n2
        #updates values
        n1 = n2
        n2 = nth
        count += 1
