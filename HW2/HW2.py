
# coding: utf-8

# In[ ]:

def main():
    # print command line arguments
    
    import sys

    junk1=str.split(sys.argv[2])
    junk=list(set(junk1))

    """Change the sys.argv to the same as the dataframe"""
    terminal2=[]
    year2=[]
    traffic2=[]
    for i in range(0,len(junk)):
        if junk[i] in ['T1','t1']:
            terminal2.append('Terminal 1')
        elif junk[i] in ['T2','t2']:
            terminal2.append('Terminal 2')
        elif junk[i] in ['T3','t3']:
            terminal2.append('Terminal 3')
        elif junk[i] in ['T4','t4']:
            terminal2.append('Terminal 4')
        elif junk[i] in ['T5','t5']:
            terminal2.append('Terminal 5')
        elif junk[i] in ['T6','t6']:
            terminal2.append('Terminal 6')
        elif junk[i] in ['TBI','tbi']:
            terminal2.append('Tom Bradley International Terminal')
        elif junk[i] in ['2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016']:
            year2.append(junk[i])
            year2=[int(float(x)) for x in year2]
        elif junk[i] in ['departure']:
            traffic2.append('Departure')
        elif junk[i] in ['arrival']:
            traffic2.append('Arrival')

    """If [] then change to all"""
    if len(terminal2)==0:
        terminal2=['Terminal 1','Terminal 2','Terminal 3','Terminal 4','Terminal 5','Terminal 6','Tom Bradley International Terminal']
    if len(year2)==0:
        year2=[2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]
    if len(traffic2)==0:
        traffic2=['Departure','Arrival']
    
    """define the median, mean, std function"""
    def median(l):
        half = len(l) // 2
        l.sort()
        if not len(l) % 2:
            return (l[half - 1] + l[half]) / 2.0
        return l[half]

    def mean(data):
        """Return the sample arithmetic mean of data."""
        n = len(data)
        if n < 1:
            raise ValueError('mean requires at least one data point')
        return sum(data)/n # in Python 2 use sum(data)/float(n)

    def _ss(data):
        """Return sum of square deviations of sequence data."""
        c = mean(data)
        ss = sum((x-c)**2 for x in data)
        return ss

    def pstdev(data):
        """Calculates the population standard deviation."""
        n = len(data)
        if n < 2:
            raise ValueError('variance requires at least two data points')
        ss = _ss(data)
        pvar = ss/n # the population variance
        return pvar**0.5

    import json
    """f=open('/Users/huahao/Desktop/USC Class/INF551/HW/HW2/lax.json')"""
    f=open(sys.argv[1])
    lax=json.load(f)

    ID=[]
    Date=[]
    Terminal=[]
    Arrival=[]
    Domestic=[]
    number=[]
    for i in lax["data"]:
        ID.append(i[0])
        Date.append(i[9])
        Terminal.append(i[10])
        Arrival.append(i[11])
        Domestic.append(i[12])
        number.append(i[13])
    year=[x[0:4] for x in Date]
    year=[float(x) for x in year]
    number = [float(x) for x in number]

    lst = [item[0] for item in [Terminal,year,Arrival]]
    listoflist=[]
    lst=[]

    for i in range(0,len(ID)):
        lst=[item[i] for item in [Terminal,year,Arrival,number]]
        listoflist.append(lst)

    result_dict=dict(zip(ID, listoflist))
    
    """This step generate the final dataframe"""
    final=dict((k, v) for k, v in result_dict.items() if (v[0] == 'Terminal 1' or v[0] == 'Terminal 2' or v[0] == 'Terminal 3' or v[0] == 'Terminal 4' or v[0] == 'Terminal 5' or v[0] == 'Terminal 6' or v[0] == 'Tom Bradley International Terminal'))
    
    """This section is what you want to edit"""
    d = dict((k, v) for k, v in final.items() if (v[0] in terminal2 and v[1] in year2 and v[2] in traffic2))
    
    nplan=[]
    for key, value in d.items():
        nplan.append(value[3])
    
    num1=min(nplan)
    split_num1=str(num1).split('.')
    int_part1=int(split_num1[0])

    num2=max(nplan)
    split_num2=str(num2).split('.')
    int_part2=int(split_num2[0])

    print(int_part1,int_part2,median(nplan),round(mean(nplan),2),round(pstdev(nplan),2)) 

if __name__ == '__main__':
    main()
    

