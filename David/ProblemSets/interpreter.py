def main():
    equation = input("Expression: ")
    x = float(equation.split(" ")[0])
    y = equation.split(" ")[1]
    z = float(equation.split(" ")[2])

    match y:
        case "+":
            ans = x+z
        case "-":
            ans = x-z
        case "*":
            ans = x*z
        case "/":
            ans = x/z
    ans = round(ans,1)
    print(ans)

main()
