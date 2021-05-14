# Enter your code here. Read input from STDIN. Print output to STDOUT
import math


def main():
    sample, mean, std, interval, z = [float(input()) for i in range(5)]
    # https://en.wikipedia.org/wiki/Standard_score#Prediction_intervals
    # A < X < B  ==> A = u+zo, B = u - zo
    a = mean - (z * (std / math.sqrt(sample)))
    b = mean + (z * (std / math.sqrt(sample)))
    print(round(a, 2)) # 484.32
    print(round(b, 2)) # 515.68


def phi(x, u, o):
    return (1.0 + math.erf(
        (x - u) / (o * math.sqrt(2.0))
    )) / 2.0


main()
