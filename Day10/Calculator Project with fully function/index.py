from replit import clear
#creating a calculator using function, dictionary, and while loop,conditional statement
def addition(num1,num2):
    """To perform addition"""
    return num1+num2
def substraction(num1,num2):
    """To perform substraction"""
    return num1-num2
def multiplication(num1,num2):
    """To perform multiplication"""
    return num1*num2
def division(num1,num2):
    """To perform division"""
    return num1/num2

operation={
    '+':addition,
    '-':substraction,
    '*':multiplication,
    '/':division
}
start=True
while start:
    num1=int(input("Enter first number:"))
    for operator in operation:
        print(operator)
    select_symbol=input("Select a operation:")
    num2=int(input("Enter next number:"))
    calculation_function=operation[select_symbol]
    answer=calculation_function(num1,num2)
    print(f"{num1} {select_symbol} {num2} = {answer}")

    to_continue=True
    while to_continue:
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")=='y':
            num1=answer
            select_symbol=input("Select a operation:")
            num2=int(input("Enter next number:"))
            calculation_function=operation[select_symbol]
            answer=calculation_function(num1,num2)
            print(f"{num1} {select_symbol} {num2} = {answer}")
        else:
            to_continue=False
            clear()
            start=True