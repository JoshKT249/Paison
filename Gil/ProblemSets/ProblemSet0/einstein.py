def main():
    Smart = int(input("m: "))
    print("E:", algorithm(Smart))

def algorithm(c):
    return c * pow(300000000, 2)

main()