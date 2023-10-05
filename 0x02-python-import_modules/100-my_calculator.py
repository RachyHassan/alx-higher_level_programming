#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    ope = {"+": add, "-": sub, "*": mul, "/": div}
    operator = sys.argv[2]

    if operator not in ope:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    output = ope[operator](a, b)

    print("{} {} {} = {}".format(a, operator, b, result))
