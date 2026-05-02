def get_operation():
    while True:
        try:
            inp = int(input("Choose operation (1=add, 2=sub, 3=mul, 4=div, 5=pow, 6=exit): "))
            if inp in [1,2,3,4,5,6]:
                return inp
            print('enter num bet 1-6')
        except ValueError:
            print('enter ints only bet 1-6')
def get_input():
    while True:
        try:
            data = list(map(float,input('enter space separated vals.').split()))
            return data 
        except ValueError:
            print('enter only float values')
def perform_operation(data,inp):
    while True:
        if inp == 1:  # Addition
            res = 0
            for num in data:
                res += num
            return res    
        elif inp == 2:  # Subtraction
            res = data[0]
            for num in data[1:]:
                res -= num
            return res    
    
        elif inp == 3:  # Multiplication
            res = 1
            for num in data:
                res *= num
            return res    
    
        elif inp == 4:  # Division
            if len(data) != 2:
                return 'only 2 nums' 
                break
            try:
                return data[0] / data[1]
            except ZeroDivisionError:
                return 'cannot divide zero'    
    
        elif inp == 5:  # Power
            if len(data) != 2:
                return "Enter exactly 2 numbers"
            return data[0] ** data[1]
    
        elif inp == 6:
            return None
        else:
            return "Invalid operation"
            

def display_result(result):
    print(result)

data = get_input()
while True:
    inp = get_operation()
    result = perform_operation(data,inp)
    if result is not None:
        display_result(result)
    else:
        exit()
