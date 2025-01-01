import art
from replit import clear
start=True
while start:
    print(art.logo)
    num1=int(input("What is the first number:"))
    print("+ \n- \n* \n/")
    selected_operator=input("pick an operation:")
    num2=int(input("What is the second number:"))
    def calculation(num1,num2):
        if selected_operator=='+':
            return num1+num2
        elif selected_operator=='-':
            return num1-num2
        elif selected_operator=='*':
            return num1*num2
        elif selected_operator=='/':
            return num1/num2
        return "invalid operation"
        
    output=calculation(num1,num2)
    print(output)

    should_continue=True
    while should_continue:
        if input(f"Do you want to continue with {output}? type 'yes' or 'no':")=='yes':
            #override the default behavior of the form
            selected_operator=input("pick an operation:")
            num1=output
            num2=int(input("What is the second number:"))
            output=calculation(num1,num2)
            print(f"{num1} {selected_operator} {num2} = {output}")
        else:
            should_continue=False
            clear()
            start=True


