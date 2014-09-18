""" Function, that checking if number is between "a" and "b" """
def input_int(a, b):
    print("Enter number between {0} and {1}".format(a, b) )
    while True:
        x = input()
        if x.isdigit():
            x = int(x)
            if a <= x <= b:
                return x
            else:
                print("Enter number only between {0} and {1}!".format(a, b) )
        else:
            print("Enter only numbers!")
num1 = 1
num2 = 100
usrnum = input_int(num1, num2)
print("Our number is {0}".format(usrnum) )

input()
