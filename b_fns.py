# Calculator function
# Clean the function
# Write tests
# Implement substraction and multiplication
# for multiplication allow operators to be x,X or *

def calc(num1:int, num2:int, op:str) -> int|str:
    try:
        if op == "+":
            return num1+num2
        if op == "/":
            return num1/num2
        if op in "xX*":
            return num1*num2
        return "Operation not allowed"
    except Exception as e:
        return f"***** Error: {e}"

def log_this(to_log: str) -> None:
    """
    Function to log to file log.txt
    Paramenters
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