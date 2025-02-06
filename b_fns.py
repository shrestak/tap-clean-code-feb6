# Calculator function
# Clean the function
# Write tests
# Implement substraction and multiplication - Try
# for multiplication allow operators to be x,X or * - Try

def calc(num1: int, num2: int, op:str) -> int|str:
    """
    Function to calculate
    Parameters:
        num1 = number
        num2 = number
        op = string which is +, -, /, x/X,*
    """
    try:
        if op == "+":
            return num1+num2
        if op == "/":
            if num2==0:
                return "ZeroDivision not possible"
            return num1/num2
        if op in "xX*":
            return num1 * num2
        return "Operation not allowed"
    except Exception as e:
        return f"**** ERROR: {e}"

def log_this(to_log: str) -> None:
    """
    Function to log to file log.txt
    Parameters:
        to_log: String to log
    """
    # f = open("log.txt", "+a")
    # log_txt = f"6+2={res}\n"
    # f.write(log_txt)
    # return res
    with open("log.txt", "+a") as file_pointer:
        file_pointer.write(to_log)

print(f"6+2={calc(6, 2, "+")}")
print(f"6/2={calc(6, 2, "/")}")
# print(f"6+2={calc('6', 2, "+")}")
# print(f"6-2={calc(6, 2, "-")}")
# print(f"6*2={calc(6, 2, "x")}")
# print(f"6*2={calc(6, 2, "d")}")
