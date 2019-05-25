h=float(input("Ingrese el valor h: ")) #Se ingresa el valor de h
valor_final=float(input("Ingresa el valor de Y que desea obtener: ")) #valor hasta el cual acabara la tabla
xi=int(input("Declare el valor inicial de Xi: ")) #Variable que indicia el inicio de Xi
####################################Arreglo para automatizar el espacio de arrays###############
j=0
valor_temp=0
while (valor_temp!=valor_final):
    j=j+1
    valor_temp=valor_temp+h
####################################Declaracion de espacio automatico de arrays#################
temp=float(xi)
ArrayXi=[0 for i in range(j+1)]
ArrayYiP=[0 for i in range(j+1)]
ArrayFiP=[0 for i in range(j+1)]
ArrayYiC=[0 for i in range(j+1)]
ArrayFiC=[0 for i in range(j+1)]
#############################Define base#########################################################
def f(x,y):
    r=float((1/2)*(1+x)*y**2)#Funcion f(x,y) CAMBIA ESTA FUNCION SI ES NECESARIO
    return r
def predictor(i):
    r= float(ArrayYiC[i-3]+((4*h)/3)*(2*ArrayFiC[i-2] -ArrayFiC[i-1] + 2*ArrayFiC[i]))#formula de predictor para Milne-Simpson
    return r
def corrector(i):
    r = float((ArrayYiC[i-1])+(h/3)*(ArrayFiC[i-1] +(4*ArrayFiC[i]) + ArrayFiP[i+1]))#formula de corrector para Milne-Simpson
    return r
#################################################################################################
sum=0
for i in range(j+1): #se generan en el array de XI sus respectivos valores partiendo de 0 con sus brincos dependiendo valor de h
    ArrayXi[i]=round(temp,2)
    temp=temp+h
for i in range (xi,xi+4): #Se ingresan los valores iniciales de y
    ArrayYiC[i]=float(input("Ingrese el valor y(%s): "%(sum)))
    sum=round(sum+h,4)

for i in range (xi,xi+4): #se generan los valores de Fi corrector automaticamente dado datos los valores de y(0),y(0+h),y(0+2h),y(0+3h)
    ArrayFiC[i]=round(f(ArrayXi[i],ArrayYiC[i]),10)
###################################################################################################################################
for i in range (xi+4,j+1):
    ArrayYiP[i]=round(predictor(i-1),10)#Este array llena la columna de Yi predictor usando la funcion predictor
    ArrayFiP[i]=round(f(ArrayXi[i],ArrayYiP[i]),10)#Este array llena la columna de Fi predictor usando la funcion f(x,y)
    ArrayYiC[i]=round(corrector(i-1),10)#Este array llena la columna de Yi corrector usando la funcion corrector
    ArrayFiC[i]=round(f(ArrayXi[i],ArrayYiC[i]),10)#Este array llena la columna de Fi corrector usando la funcion f(x,y)
###########################################Variables para colocar nombre de encabezados de la tabla reservando espacios##############
t1="i"
t2="xi"
t3="Yi,P"
t4="Fi,P"
t5="Yi,C"
t6="Fi,C"
print("| %-4s| %-4s | %-18s | %-19s | %-19s | %-19s |" %(t1,t2,t3,t4,t5,t6))#imprimir encabezado
#############################Imprimir los valores de los array en forma de tabla#####################################################
for i in range(0,j+1):
    print("| %-4s| %-4s | %-18s | %-19s | %-19s | %-19s |" %(i,ArrayXi[i],ArrayYiP[i],ArrayFiP[i],ArrayYiC[i],ArrayFiC[i]))



