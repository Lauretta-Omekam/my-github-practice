art = """

 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
          _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                              
"""

def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2
operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}
#operations["*"]= mul(4,8)
#print(operations["*"])

def calculator():
    print(art)
    should_continue = True
    num1 = float(input("Enter the first number:  "))
    while should_continue:
        for symbols in operations:
            print(symbols)
        symbol = input("Select an operation:  ")
        num2 = float(input("Enter the second number:  "))
        answer = operations[symbol](num1, num2)
        print(f"{num1} {symbol} {num2} = {answer} ")

        choice = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new operation").lower()
        if choice == "y":
            num1 = answer
        else:
            should_continue = False
            print("\n"*20)
            calculator()
calculator()