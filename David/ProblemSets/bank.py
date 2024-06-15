def main():
    greeting = input("Greeting: ")
    greeting = greeting.casefold().strip()
    if starthello(greeting) == True:
        print("$0")
    elif starth(greeting) == True:
        print("$20")
    else:
        print("$100")

def starthello(string):
    if string[:5] == "hello":
        return True

def starth(string):
    if string[:1] == "h":
        return True

main()
