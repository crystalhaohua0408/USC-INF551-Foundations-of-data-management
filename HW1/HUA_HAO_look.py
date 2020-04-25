import sys
f=open(sys.argv[1])
lines=f.readlines()
Start=int(lines[0])
Request_list=lines[1].strip().split(",")
Request=[]
for item in Request_list:
    Request.append(int(item))

if __name__ == '__main__':
    high=199
    low=0
    n_Start=Request.count(Start)
    
    if n_Start==0:
        templist=Request
        templist.sort()
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
        high=199
        low=0
        distance_high=abs(high-Start)
        distance_low=abs(Start-low)

        if distance_high<distance_low:
            n = len(Request)                           # Number of Requests
            Order = []
            n_Start=Request.count(Start)
            Start_list=[Start]*n_Start
            Order.extend(Start_list)

            k = Start + 1
            while k < 200:                          # Diskhead moving inward from
                for l in range(0,n):                # previous position
                    if(Request[l] == k):            # Request found
                        Order.append(k)             # Request executed
                k += 1

            i = Start - 1
            while i > 0:                            # Diskhead moving outward from start
                for j in range(0,n):                    #position
                    if(Request[j] == i):            # Request found
                        Order.append(i)             # Request executed

                i -= 1

            Sum = 0
            for p in range(0,len(Order) - 1):
                Sum += abs(Order[p] - Order[p+1])   # Calculates total movement
            print('Order:%s'%Order)
            print('Sum:%d'%Sum)

        else:
            n = len(Request)                        # Number of Requests
            Order = []
            n_Start=Request.count(Start)
            Start_list=[Start]*n_Start
            Order.extend(Start_list)

            i = Start - 1
            while i > 0:                            # Diskhead moving outward from start
                for j in range(0,n):                # position
                    if(Request[j] == i):            # Request found
                        Order.append(i)             # Request executed
                i -= 1

            k = Start + 1
            while k < 200:                          # Diskhead moving inward from
                for l in range(0,n):                #previous position
                    if(Request[l] == k):            # Request found
                        Order.append(k)             # Request executed
                k += 1

            Sum = 0
            for p in range(0,len(Order) - 1):
                Sum += abs(Order[p] - Order[p+1])   # Calculates total movement
            print('Order:%s'%Order)
            print('Sum:%d'%Sum)       
