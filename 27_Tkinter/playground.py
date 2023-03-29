def main():
    print(add(3, 30, 300))
    print(calculate(5, add = 10, multiply = 10, divide = 5))
    pass

def add(*args: int) -> int:
    s = 0
    for i in args:
        s += i
    return s
    
# Unlimited.. keyword arguments?
def calculate(n: int, **kwargs) -> int:
    
    # Arguments are passed as a dictionary
    for k, v in kwargs.items():
        if k == "add":
            n += v
        elif k == "multiply":
            n *= v
        elif k == "divide":
            n //= v
        elif k == "subtract":
            n -= v
        else:
            continue
    return n

main()