def main():
    answer = input("Expression: ")
    x, y, z = answer.split()
    if y == "+":
        result = int(x) + int(z)
        print(f"{result:.1f}")
    elif y == "-":
        result = int(x) - int(z)
        print(f"{result:.1f}")
    elif y == "*":
        result = int(x) * int(z)
        print(f"{result:.1f}")
    elif y == "/":
        result = int(x) / int(z)
        print(f"{result:.1f}")

if __name__ == "__main__":
    main()