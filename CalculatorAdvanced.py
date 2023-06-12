def add(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def multi(n1,n2):
    return n1 * n2

def div(n1,n2):
    return n1 / n2

dictionary = {
    '+' : add,
    '-' : sub,
    '*' : multi,
    '/' : div,
}
def func():
    num1 = float(input('Whats the first number: '))

    continue_ = True
    while continue_:

        operation_symbol = input("Choose an operator: ")
        num2 = float(input("Whats the next number?: "))
        cal = dictionary[operation_symbol]
        answer1 = cal(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer1}")
        
        inp = input("Do you want to continue with the answer or start over?(Y/N): ")
        if inp == 'y':
            pass
        else:
            continue_ = False
            func()
        num1 = answer1

func()

