def main():
    answer = input("What is the answer blah blah blah? ").lower()
    if answer == "42" or answer == "forty-two" or answer == "forty two":
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()