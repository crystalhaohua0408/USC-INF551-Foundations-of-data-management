import sys
f=open(sys.argv[1])
lines=f.readlines()
Start=int(lines[0])
Request_list=lines[1].strip().split(",")
Request=[]
for item in Request_list:
    Request.append(int(item))

if __name__ == '__main__':
    distance_high=abs(Start-199)
    distance_low=abs(Start-0)
    templist = sorted(Request)
    n_Start=templist.count(Start)
    
    if n_Start==0:
        templist = sorted(Request)
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

    else:
        templist=sorted(Request)
        position=Start
        Order=[]
        Start_list=[Start]*n_Start
        Order.extend(Start_list)
        templist_new=[x for x in templist if x not in Start_list]
        if distance_high<distance_low:
            while len(templist_new)>0:
                a=[abs(x-position) for x in templist_new]
                value=list((v) for i,v in enumerate(a))
                indices=[i for i, x in enumerate(value) if x == min((v) for i,v in enumerate(a))]   
                if len(indices)!=1:
                    index=max([i for i, x in enumerate(value) if x == min((v) for i,v in enumerate(a))])
                    newposition=templist_new[index]
                    Order.append(newposition)
                    position=newposition
                    print(position)
                    templist_new.remove(newposition)

                else:
                    while len(templist_new)>0:
                        a=[abs(x-position) for x in templist_new]
                        junk = min((v,i) for i,v in enumerate(a))
                        index=junk[1]
                        newposition=templist_new[index]
                        Order.append(newposition)
                        position=newposition
                        templist_new.remove(newposition)
        
            Sum = 0
            for p in range(0,len(Order) - 1):
                Sum += abs(Order[p] - Order[p+1])   # Calculates total movement
            print('Order:%s'%Order)
            print('Sum:%d'%Sum)

        else:
            while len(templist_new)>0:
                a=[abs(x-position) for x in templist_new]
                value=list((v) for i,v in enumerate(a))
                indices=[i for i, x in enumerate(value) if x == min((v) for i,v in enumerate(a))]   
                if len(indices)!=1:
                    index=min([i for i, x in enumerate(value) if x == min((v) for i,v in enumerate(a))])
                    newposition=templist_new[index]
                    Order.append(newposition)
                    position=newposition
                    templist_new.remove(newposition)
                else:
                    while len(templist_new)>0:
                        a=[abs(x-position) for x in templist_new]
                        junk = min((v,i) for i,v in enumerate(a))
                        index=junk[1]
                        newposition=templist_new[index]
                        Order.append(newposition)
                        position=newposition
                        templist_new.remove(newposition)
        
            Sum = 0
            for p in range(0,len(Order) - 1):
                Sum += abs(Order[p] - Order[p+1])   # Calculates total movement
            print('Order:%s'%Order)
            print('Sum:%d'%Sum)  
