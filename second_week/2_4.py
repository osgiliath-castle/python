""" fibo function without recursion """

def fibo():
    a, b = 1, 1
    num = eval(input("Please input what Fib number you want to be calculated: "))
    num_int = int(num - 2)
    
    for i in range(num_int):
        
        a, b = b, a + b
        
    print(b)



