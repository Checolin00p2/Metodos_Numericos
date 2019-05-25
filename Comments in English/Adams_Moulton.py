
h=float(input("Ingrese el valor h: ")) #Into value of h
valor_final=float(input("Ingresa el valor de Y que desea obtener: ")) #Enter value until where will finish table
xi=int(input("Declare el valor inicial de Xi: ")) #Start tabulation of Xi
####################################Declarate automated space of each list###############
j=0
valor_temp=0
while (valor_temp!=valor_final):
    j=j+1
    valor_temp=valor_temp+h
temp=float(xi)
####################################Declaration of space into list#################
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
sum=0#Indicates the coordinate in the input
for i in range(j+1): #Generate values into array Xi
    ArrayXi[i]=round(temp,2)
    temp=temp+h
for i in range (xi,xi+4): #Enter values main in the array Yi,c
    ArrayYiC[i]=float(input("Ingrese el valor y(%s): "%(sum)))
    sum=round((sum+h),2)

for i in range (xi,xi+4): #Generate the values of Fi corrector automatically given the data of the values ​​of y(0),y(0+h),y(0+2h),y(0+3h)
    ArrayFiC[i]=round(f(ArrayXi[i],ArrayYiC[i]),10)
############################################Array to fill list##############################################################
for i in range (xi+4,j+1):
    ArrayYiP[i]=round(predictor(i-1),10)#this array fill the  column of Yi predictor using the function predictor
    ArrayFiP[i]=round(f(ArrayXi[i],ArrayYiP[i]),10)#this array fill the  column of Fi predictor using the function f(x,y)
    ArrayYiC[i]=round(corrector(i-1),10)#this array fill the  column of Yi corrector using the function corrector
    ArrayFiC[i]=round(f(ArrayXi[i],ArrayYiC[i]),10)#this array fill the  column of Fi corrector using the function f(x,y)
###########################################variables to place table header reserving spaces ##############
t1="i"
t2="xi"
t3="Yi,P"
t4="Fi,P"
t5="Yi,C"
t6="Fi,C"
print("| %-4s| %-4s | %-18s | %-19s | %-19s | %-19s |" %(t1,t2,t3,t4,t5,t6))#print header
#############################print values of list in form of table#####################################################
for i in range(0,j+1):
    print("| %-4s| %-4s | %-18s | %-19s | %-19s | %-19s |" %(i,ArrayXi[i],ArrayYiP[i],ArrayFiP[i],ArrayYiC[i],ArrayFiC[i]))



