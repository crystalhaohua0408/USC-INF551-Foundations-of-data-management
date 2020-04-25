import sys
f=open(sys.argv[1])
lines=f.readlines()
Start=int(lines[0])
Request_list=lines[1].strip().split(",")
Request=[]
for item in Request_list:
    Request.append(int(item))

if __name__ == '__main__':
    n = len(Request)
    Order = []
    Request_tmp=sorted(Request)
    n_Start=Request.count(Start)

    if n_Start==n:
        templist=sorted(Request)
        position=Start
        Order=[]
        Sum=0
        while len(templist)>0:
            a=[abs(x-position) for x in templist]
            junk = min((v,i) for i,v in enumerate(a))
            index=junk[1]
            newposition=templist[index]
            Order.append(newposition)
            Sum+=abs(position-newposition)
            position=newposition
            templist.remove(newposition)
        print('Order:%s'%Order)
        print('Sum:%d'%Sum)

    elif n_Start==0:
        No_order=[0,199,Start]
        if Start != 0 and Start < Request_tmp[n-1]:
            Request_tmp.append (0)
        Order.append(Start)
        p = len(Request_tmp)
        print(Request_tmp)
    
        k = Start+1
        while k <200:
            if(k == 199):
                Order.append(k)
            for l in range(0,n):
                if(Request[l] == k):
                    Order.append(k)
            k += 1

        i=0
        Order.append(i)
        while i < Start-1:
            for j in range(0,n):            
                if(Request[j] == i):            
                    Order.append(i)
            i += 1

        Sum = 0
        for p in range(0,len(Order) - 1):
            Sum += abs(Order[p] - Order[p+1])   # Calculates total movement

        Order2=[x for x in Order if x not in No_order] 
        print('Order:%s'%Order2)
        print('Sum:%d'%Sum)

    else:
        No_order=[0,199]
        Start_list=[Start]*n_Start
        Order.extend(Start_list)
        if Start != 0 and Start < Request_tmp[n-1]:
            Request_tmp.append (0)
        p = len(Request_tmp)
    
        k = Start+1
        while k <200:
            if(k == 199):
                Order.append(k)
            for l in range(0,n):
                if(Request[l] == k):
                    Order.append(k)
            k += 1

        i=0
        Order.append(i)
        while i < Start-1:
            for j in range(0,n):            
                if(Request[j] == i):            
                    Order.append(i)
            i += 1

        Sum = 0
        for p in range(0,len(Order) - 1):
            Sum += abs(Order[p] - Order[p+1])   # Calculates total movement

        Order2=[x for x in Order if x not in No_order] 
        print('Order:%s'%Order2)
        print('Sum:%d'%Sum)
    

    


    
    

    

    
    
