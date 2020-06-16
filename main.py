def bill_count(amount,bills):
    bills=bills[ : :-1]
    sum=0
    for i in bills:
        if int(amount/i) >0:
            sum=sum+int(amount/i)
            amount=amount%i
    print(sum)
a=int(input("enter the amount:"))
if a<0:
    print("please enter a positive amount")
    a=int(input("enter the amount:"))
b = [] 
c= [1,2,5,10,20,50,100,2000]
n = int(input("Enter number of bills : "))
print("enter the bills one by one")
for i in range(0, n): 
    ele = int(input("enter the bill:")) 
    if ele not in c:
        print("please enter the indian currency")
        ele = int(input("enter the element"))
    b.append(ele)
    b.sort()
if min(b)>a:    
    print("please enter the correct list of bills")
    for i in range(0, n): 
        ele = int(input("enter the element:")) 
        if ele not in c:
           print("please enter the indian currency")
           ele = int(input("enter the element"))
        b.append(ele)
        b.sort()
bill_count(a,b)  