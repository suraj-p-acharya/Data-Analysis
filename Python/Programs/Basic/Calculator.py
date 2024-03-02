# All Imports command go in this block.


#Function Used in this program go in here.
def Calculator(a,b,Operator):
    match Operator:
        case "+":
            return a+b
        case "-":
            return a-b
        case "*":
            return a*b
        case "/":
            return a/b
        case "%":
            return str(a/b*100) + "%"
        

#All Input commands go in this block.
print("Input First Number:", end = " ")
a=int(input())
print("Input Second Number:", end = " ")
b = int(input())
print("Input Operator (+,-,*,/,%):", end = " ")
Operator=str(input())
print(Calculator(a,b,Operator))