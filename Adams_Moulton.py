j=4
i=0
ArrayXi=[0 for i in range(j+1)]
ArrayYiP=[0 for i in range(j+1)]
ArrayFiP=[0 for i in range(j+1)]
ArrayYiC=[0 for i in range(j+1)]
ArrayFiC=[0 for i in range(j+1)]
#############################Define base#########################################################
def f(x,y):
    r=float(2*y-2*x-1)
    return r
def predictor(i):
    r= float(ArrayYiC[i]+(h/24)*(55*ArrayFiC[i] -59*ArrayFiC[i-1] + 37*ArrayFiC[i-2]- 9*ArrayFiC[i-3]))
    return r
    
def corrector(i):
    r = float(ArrayYiC[i]+(h/24)*(9*ArrayFiP[i+1] + 19*ArrayFiC[i] - 5*ArrayFiC[i-1] + ArrayFiC[i-2]))
    print("%s %s %s %s %s" % (ArrayYiC[i],ArrayFiP[i+1],ArrayFiC[i],ArrayFiC[i-1],ArrayFiC[i-2]))
    return r
#################################################################################################

xi=float(0.0)
sum=0

h=float(input("Ingrese el valor h: ")) #Se ingresa el valor de h

for i in range(j+1): #se generan en el array de XI sus respectivos valores partiendo de 0 con sus brincos dependiendo valor de h
    ArrayXi[i]=round(xi,2)
    xi=xi+h
for i in range (0,4): #Se ingresan los valores iniciales de y
    ArrayYiC[i]=float(input("Ingrese el valor y(%s): "%(sum)))
    sum=round((sum+h),2)

for i in range (0,4): #se generan los valores de Fi corrector automaticamente dado datos los valores de y(0),y(0+h),y(0+2h),y(0+3h)
    ArrayFiC[i]=round(f(ArrayXi[i],ArrayYiC[i]),10)
###################################################################################################################################

for i in range (4,j+1):
    ArrayYiP[i]=round(predictor(i-1),10)
    ArrayFiP[i]=round(f(ArrayXi[i],ArrayYiP[i]),10)
    ArrayYiC[i]=round(corrector(i-1),10)
    ArrayFiC[i]=round(f(ArrayXi[i],ArrayYiC[i]),10)
    print("%s %s" %(ArrayXi[i],ArrayYiC[i]))


t1="i"
t2="xi"
t3="Yi,P"
t4="Fi,P"
t5="Yi,C"
t6="Fi,C"
i=0

#print("%-15s %-15s %s" %(titleProduct, titleItems, titleCost))
print("| %-4s| %-4s | %-18s | %-19s | %-19s | %-19s |" %(t1,t2,t3,t4,t5,t6))

for i in range(j+1):
    print("| %-4s| %-4s | %-18s | %-19s | %-19s | %-19s |" %(i,ArrayXi[i],ArrayYiP[i],ArrayFiP[i],ArrayYiC[i],ArrayFiC[i]))



