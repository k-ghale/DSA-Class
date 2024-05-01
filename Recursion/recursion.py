
def fact(n):
    if(n < 1):
        return 1;
    
    return n * fact(n-1);

print(fact(5));

def fib(n):
    if(n < 2):
        return 1;
    
    return fib(n-1) + fib(n-2);


print(fib(5));

def Toh(n,start_rod,inter,dest_rod):
    if(n == 0):
        return;
    
    Toh(n-1,start_rod,dest_rod,inter);
    print("Disk",n,"moved from",start_rod,"to",inter);
    return Toh(n-1,dest_rod,inter,start_rod);

Toh(4,'A','B','C');


def factorial(num):
    if(num < 1):
        return 1;
    return num * factorial(num-1);

print(factorial(10));
