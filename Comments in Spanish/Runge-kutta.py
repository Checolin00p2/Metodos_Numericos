xi=float(0.0)
yi=float(2.0)
h=float(0.25)

def f(x,y):
    r=float(1/(x+y))
    return r
def incremento(y,h,v1,v2,v3,v4):
    r = float(y+((h/6))*(v1+(2*v2)+(2*v3)+v4))
    return r
t1="i"
t2="xi"
t3="yi"
t4="k1"
t5="k2"
t6="k3"
t7="k4"
i=0
#print("%-15s %-15s %s" %(titleProduct, titleItems, titleCost))
print("| %-2s| %-4s | %-18s | %-19s | %-19s | %-19s | %-19s|" %(t1,t2,t3,t4,t5,t6,t7))
print("------------------------------------------------------------------------------------------------------------------------")
while(xi<=1):
    k1=float(f(xi,yi))
    k2=float(f((xi+(h/2)),(yi+((h*k1)/2))))
    k3=float(f((xi+(h/2)),(yi+((h*k2)/2))))
    k4=float(f((xi+h),(yi+(h*k3))))
    print("| %-2d| %-4s | %-18s | %-19s | %-19s | %-19s | %-19s|" %(i,xi,yi,k1,k2,k3,k4))
    yi=incremento(yi,h,k1,k2,k3,k4)
    if (xi==1):
        print("------------------------------------------------------------------------------------------------------------------------")
    i=i+1
    xi=xi+h
