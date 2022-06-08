# Student: Tomer Handali ID: 206751489
# Question recieved: 7+5=12

import   math


def Bisection_Method(polynom,start_point , end_point,epsilon):

    a=start_point
    b=end_point
    f=polynom


    max_iteration = math.ceil(- (math.log(epsilon/(end_point-start_point),math.e)/math.log(2,math.e))-1)


    for i in range(1,max_iteration+1):
        c=(a+b)/2
        print('iteration ',i,' | a: ',a,' | b: ',b,' | mid: ',c,' | f(a): ',f(a),' | f(b): ',f(b),' | f(c): ',f(c))

        if f(a)*f(c)<0:
            b=c
        elif f(b)*f(c)<0:
            a=c
        elif (f(c) == 0) or math.fabs(a-b)<epsilon:
            print('Solution: ',c)
            return c
        else:
            print('Bisection method failed')
            return None

    c = (a+b)/2
    print('Solution: ',c)
    return c
def secant_method(polynom , x0,x1,epsilon):

    max_iteration = math.ceil(- (math.log(epsilon / (x1 - x0), math.e) / math.log(2, math.e)) - 1)

    f=polynom


    a=x0
    b=x1

    for i in range(1,max_iteration+1):
        if(f(b)-f(a)==0):
            break
        xn = (a*f(b)-b*f(a))/(f(b)-f(a))

        print('iteration ', i, ' | x(i-1): ', a, ' | x(i): ', b, ' | x(i+1): ', xn)
        if f(xn)==0 or math.fabs(b-a)< epsilon:
            print('Solution: ',xn)
            return xn
        a=b
        b=xn

    print('Solution: ',xn)
    return xn


    print('Solution: ',xn)
    return xn

def start(f, start_point,end_point,epsilon):


    sus = []
    x0 = start_point
    x1 = start_point+0.1

    while x1 < end_point:
        if f(x0)*f(x1)<0:
            z=[x0,x1]
            sus.append(z)

        x1 += 0.1
        x0 += 0.1

    while True:
        print('How would you like to find the roots of the polynom: ')
        print('1. Bisection method')
        print('2. Secant method')
        print('0. Exit')

        choice = int(input())
        if choice ==0:
            break
        if choice>2 or choice<0:
            print('bad input try again')
            continue

        if choice == 1:
            for element in sus:
                Bisection_Method(f,element[0],element[1],epsilon)
                print('')


        if choice==2:

            for element in sus:
                secant_method(f,element[0],element[1],epsilon)
                print('')


def my_f(x): #question 12 function
    return (2 * x * math.pow(math.e,(-x)) + math.log(2*math.pow(x,2),math.e))*(2*math.pow(x,4) + 2*math.pow(x,2) - 3*x - 5)

eps = math.pow(10,-10)
start_point = 0+ eps
end_point = 1.5

start(my_f,start_point,end_point,eps)