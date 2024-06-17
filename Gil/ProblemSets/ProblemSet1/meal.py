def main():
    time = input("What time is it?")
    number = convert(time)
    if 7 <= number <= 8:
        print("breakfast time")
    elif 12 <= number <= 13:
        print("lunch time")
    elif 18 <= number <= 19:
        print("dinner time")

def convert(time):
    hours = float(time.split(":")[0])
    minutes = float(time.split(":")[1])
    time = hours + minutes/60
    return(time)


if __name__ == "__main__":
    main()