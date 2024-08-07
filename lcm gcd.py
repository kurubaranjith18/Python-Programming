def lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    while(True):
        if(greater%x==0 and greater%y==0):
            a=greater
            break
        greater+=1
    return a
num1=4
num2=2
c=lcm(num1,num2)
s=num1*num2
gcd=s/c
print("Lcm=",c)
print("Gcd=",gcd)