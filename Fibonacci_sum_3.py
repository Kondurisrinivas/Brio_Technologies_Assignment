def fibonacci3series(n):
    if n <= 0:
        return
    a = 0
    b = 1
    c = 1

    if n <= 2:
        print("Only Possible with atleast 3 numbers!!")
        return
    
   
    if n > 2:
        print("Fibonacci series whith each digit is a sum of previous 3 numbers:")
        print(a)
        print(b)
        print(c)
        for i in range(3, n):
            next_term = a + b + c
            print(next_term)
            a, b, c = b, c, next_term

terms = 50
fibonacci3series(terms)