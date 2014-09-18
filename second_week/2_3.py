""" Each step of calculating a fibonacci number is printing """

def fibo(n):
     print("Start calculating " + str(n) + "-th Fibonacci number")
     if n == 0:
         result = 0
     if n == 1:
         result = 1
     if n > 1:
         result = fibo(n - 1) + fibo(n - 2)
     print("F(" + str(n) + ") = " + str(result))
     return result
print("Enter n for calculating n-th Fibonacci number: ")

n = int(input())

print("F(" + str(n) + ") = " + str(fibo(n)))
