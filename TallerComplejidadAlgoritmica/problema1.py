import random


def main():
    array = []
    subarray = []
    sumas = []
    randomizeArray(array)
    print(array)
    sumas = sumPares(array, random.randint(0, 100))
    value = maxSum(array)
    subarray = maxCGroup(array)
    print("sumas:", sumas)
    print("Max:", value)
    print("posiciones:",subarray)
    print(factorial(5))
    print(esPrimo(367))

def randomizeArray(array):
    for i in range(0, 10):
        array.append(random.randint(0, 100))

# -----------------------------------------------------------------------------------------------------


def maxSum(array):
    maxVal = 0
    maxVal2 = 0
    for element in array:
        if element > maxVal2:
            maxVal2 = element

        if maxVal2 > maxVal:
            temp = maxVal
            maxVal = maxVal2
            maxVal2 = temp
    return maxVal + maxVal2


def maxCGroup(array):
    maxsum = 0
    positions = []
    for i in range(0, len(array)-1):
        if (array[i] + array[i+1]) > maxsum:
            maxsum = array[i] + array[i+1]

            positions = [array[i], array[i+1]]
    return positions


def sumPares(array, n):
    positions = []
    for i in range(0, len(array)-1):
        for j in range(i, len(array)-1):
            if (array[i]+array[j] == n) and i != j:
                positions.append([i, j])
    return positions


def factorial(n):
    for i in range(1, n):
        n = n * i
    return n


def esPrimo(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True
    


if __name__ == "__main__":
    main()
