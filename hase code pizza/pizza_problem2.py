#======================================================================================================================
#
#                                     ---->>  HASHCODE PIZZA PROBLEM  <<----
#                                                                               (Take the comments as a grain of salt)
#======================================================================================================================
from sys import setrecursionlimit
setrecursionlimit(10000)

def inputmod(path):   # It take path of input file and return Maximum limate (m), Number of pizzas (n), type of pissas (a[]) as variables
    a=[]
    temp=''
    f=open(path,"r")
    for x in f.read():
        if(x==' 'or x=='\n'):
            a.append(int(temp))
            temp=''
        else:
            temp=temp+x
    m=a[0]
    n=a[1]
    del a[0]
    del a[0]
    return m,n,a

def outputmod(a,path):      #It takes a list and path of file as an input and create a Output file
    f=open(path,"w")
    f.write(str(len(a))+'\n')
    for x in a:
        f.write(str(x)+' ')

def pizzatype(original,sorted):   #it takes original and sorted list and return a list with the index of elements
    sizes=[]
    original.sort()
    for x in sorted:
        for i,y in enumerate(original):
            if(x==y):
                if(i not in sizes):
                    sizes.append(i)
                    break
    sizes.sort()
    return sizes


def algomod(max,a):         #It taks a maximum limit and a list and short the list in such a way that it reaches the maximum limit
    a.sort(reverse=True)
    goodpizza=[]
    leftovers=[]
    summ=0
    for i in a:
        if(summ+i<max):
            summ+=i
            goodpizza.append(i)
        else:
            leftovers.append(i)
    if(sum==0 or goodpizza==[] or leftovers == []):
        return goodpizza
    else:
        print(goodpizza)
        print("2 :"+str(leftovers))
        leftovers=algomod(goodpizza[0]+max-summ,leftovers)
        print(goodpizza)
        print("3 :" + str(leftovers))
        for i in goodpizza:
            if(i<sum(leftovers) and sum(goodpizza)-i+sum(leftovers)<=max):
                goodpizza.remove(i)
                goodpizza.extend(leftovers)
                break
        print("max : "+str(max))
        print(goodpizza)
        print("4 :" + str(leftovers))
        return goodpizza


if(__name__== "__main__"):      #AKA Main function no introduction needed
    path=""
    path=input("Enter Input file path :")
    m,n,a=inputmod(path)
    b=algomod(m,a)
    print("main :"+str(b))
    b=pizzatype(a,b)
    outputmod(b,"answer_"+path)

#======================================================(THQ)============================================================