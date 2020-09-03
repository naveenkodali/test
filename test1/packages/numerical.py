
def narcissitic_in_given_range(lb,ub):
    nav=[]
    for i in range(lb,ub+1):
        ln=len(str(i))
        summ=0
        num=i
        for j in range(1,ln+1):
            rem=num%10
            summ+=rem**ln
            num=num//10
            if(summ>i):
                break
        if(summ==i):
            nav.append(i)
    return nav

def fact(n):
    f=1
    while(n>0):
        f=f*n
        n-=1
    return f