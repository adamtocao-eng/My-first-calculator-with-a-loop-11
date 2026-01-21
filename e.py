import sys

while True:

   questão = input("Do you wish to start the calculator?(y/n): ").lower().strip()
   if questão == 'y':
    break

   if questão == 'n':
    sys.exit()

   if questão not in ['y', 'n']:
    print("Your only options are (y) and (n), please, try again.")
     
while True:
    try:
     num1 = float(input("Add the first digits: "))

     operacao = input("Select one of the following operations (+, -, *, /): ")

     num2 = float(input("Add the last digits: "))

    except ValueError:
     print("Something is wrong, please try again.")
     continue


    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
       if num2 != 0:
        resultado = num1 / num2
       else:
        print("Division by zero is not possible.")
        resultado = None

    else:
        print("Invalid operation.")
        resultado = None

    if resultado is not None:
       print(f"Result: {resultado}")
        

    questão2 = input("Do you wish to continue?(Continue: 'y', exit: 'n'): ")
    if questão2 == 'y':
       continue
    if questão2 == 'n':
       sys.exit()