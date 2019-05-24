j=7
i=0
ArrayXi=[0 for i in range(j+1)]
ArrayYiP=[0 for i in range(j+1)]
ArrayFiP=[0 for i in range(j+1)]
ArrayYiC=[0 for i in range(j+1)]
ArrayFiC=[0 for i in range(j+1)]
#############################Define base#########################################################
def f(x,y):
    r=float((x+y)-1)
    return r
def predictor(i):
    r= float(ArrayYiC[i-3]+((4*h)/3)*(2*ArrayFiC[i-2] -ArrayFiC[i-1] + 2*ArrayFiC[i]))
    return r
def corrector(i):
    r = float((ArrayYiC[i-1])+(h/3)*(ArrayFiC[i-1] +(4*ArrayFiC[i]) + ArrayFiP[i+1]))
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
    ArrayFiC[i]=round(f(ArrayXi[i],ArrayYiC[i]),4)
###################################################################################################################################

for i in range (4,j+1):
    ArrayYiP[i]=round(predictor(i-1),6)
    ArrayFiP[i]=round(f(ArrayYiP[i],ArrayXi[i]),6)
    ArrayYiC[i]=round(corrector(i-1),6)
    ArrayFiC[i]=round(f(ArrayXi[i],ArrayYiC[i]),6)



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



