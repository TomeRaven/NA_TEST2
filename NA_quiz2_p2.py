# Student: Tomer Handali ID: 206751489
# Question recieved: 9

LX = [2.2, 3.3, 4.4, 3.5, 2.6]
LY = [1.5, 1.69, 1.9, 2.12, 2.37]
XRES = 4.5

def lagrange(X, Y, xr):
    n = len(X)
    Lmult = 1 #calculating multipliper in L calculation
    Lsum = 0 # calculating sum in P calculation
    for i in range(n):
        print("P"+str(i)+" :")
        Lmult=1
        for j in range(n):
            if i != j:
                Lres=((xr - X[j]) / (X[i] - X[j]))
                print(" L"+str(j)+" = "+str(Lres))
                Lmult *= Lres
        print("P"+str(i)+" = "+str(Lmult)+"\n")
        Lsum += Lmult*Y[i]

    print("Sum of all P and answer of lagrange method is: ",Lsum)

    return Lsum

def neville(datax, datay, x):

    n = len(datax)
    p = n*[0]
    for k in range(n):
        for i in range(n-k):
            if k == 0:
                p[i] = datay[i]
            else:
                p[i] = ((x-datax[i+k])*p[i] + (datax[i]-x)*p[i+1]) / (datax[i]-datax[i+k])

            print("P"+str(i)+str(k)+" = ",p[i])


    print("Final answer for neville method: ",p[0])
    return p[0]

lagrange(LX, LY, XRES)
#neville(LX, LY, XRES)