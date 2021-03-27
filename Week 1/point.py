from random import uniform
from math import sqrt, pow

def circleNumOfPoints(N):

    C = 0
    r = 1

    for _ in range(N):
        x = uniform(0, 1)
        y = uniform(0, 1)
        if(sqrt(pow(x, 2) + pow(y, 2) <= r)):
            C += 1

    return C/N


def getAverage(n, N):

    print()

    sum = p = 0

    for _ in range(n):

        p = circleNumOfPoints(N)
        print(f"{_+1}: {p}")
        sum += p

    print()

    return sum/n


if __name__ == '__main__':
    
    while(True):
        try:
            print("Input repeat and N point count seperated by a space.", end='\n→ ')
            n, N = input().split()

            print(f"Average: {getAverage(int(n), int(N))}\n")
        except:
            print("\nInvalid input.\n")
