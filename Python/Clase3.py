cont = 0

def main():

    print(fib(5))
    print(cont)
    print(ackerman(3,1))


def fib(n):
    global cont
    cont += 1
    if (n <= 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
def ackerman(m,n):
    if m == 0:
        return n+1
    if m > 0 and n == 0:
        return ackerman(m-1,1)
    if m > 0 and n > 0:
        return ackerman(m-1,ackerman(m,n-1))

if __name__ == '__main__':
    main()
