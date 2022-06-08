# Student: Tomer Handali, ID: 206751489


import math

def f(x):
    return (2 * x * math.pow(math.e,(-x)) + math.log(2*math.pow(x,2),math.e))*(2*math.pow(x,4) + 2*math.pow(x,2) - 3*x - 5)


# Implementing Simpson's 1/3
def simpson13(x0, xn, n):
    # calculating step size
    h = (xn - x0) / n

    # Finding sum
    integration = f(x0) + f(xn)

    for i in range(1, n):
        k = x0 + i * h

        if i % 2 == 0:
            integration = integration + 2 * f(k)
        else:
            integration = integration + 4 * f(k)

    # Finding final integration value
    integration = integration * h / 3

    return integration



lower_limit = 0.5
upper_limit = 1
sub_interval = 50


result = simpson13(lower_limit, upper_limit, sub_interval)
print("Integration result by Simpson's 1/3 method is: %0.6f" % (result))